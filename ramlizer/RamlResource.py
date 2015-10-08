from .decorators import raml_optional, raml_tabbed, raml_simple_parse
from .RamlParseable import RamlParseable
from .RamlMethod import RamlMethod
from .RamlURIParameter import RamlURIParameter


def method_parser(name):

    def parser(self):
        method = RamlMethod(self.yaml[name]) if name in self.yaml else None
        self.methods[name] = method
        setattr(self, name, method)

    parser.__name__ = 'parse_' + name
    return parser


class RamlResource(RamlParseable):

    def __init__(self, path, yaml):
        self.path = path
        self.methods = {}
        super(RamlResource, self).__init__(yaml)

    @raml_optional
    @raml_simple_parse
    def parse_displayName(self):
        pass

    @raml_optional
    @raml_simple_parse
    def parse_description(self):
        pass

    @raml_optional
    def parse_uriParameters(self):
        self.uriParameters = {x[0]: RamlURIParameter(x[1])
                              for x in self.yaml['uriParameters'].items()}

    @raml_optional
    def parse_baseUriParameters(self):
        self.baseUriParameters = {
            x[0]: RamlURIParameter(x[1])
            for x in self.yaml['baseUriParameters'].items()
        }

    parse_delete = method_parser('delete')
    parse_get = method_parser('get')
    parse_patch = method_parser('patch')
    parse_post = method_parser('post')
    parse_put = method_parser('put')

    def __str__(self):
        return '''\
[RamlResource({0.path},
    displayName:{0.displayName}
    description:{0.description}
    baseUriParameters:{0.baseUriParameters}
    uriParameters:{0.uriParameters}
    get:{0.get}
    post:{0.post}
    put:{0.put}
    delete:{0.delete}
]'''.format(self)

    @raml_tabbed
    def __repr__(self):
        return str(self)

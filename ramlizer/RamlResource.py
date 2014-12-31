#!/usr/bin/python

from decorators import raml_required, raml_optional, raml_tabbed, raml_simple_parse
from RamlParseable import RamlParseable
from RamlMethod import RamlMethod

class RamlResource(RamlParseable):

    def __init__(self, path, yaml):
        self.path = path
        self.methods = {}
        super(RamlResource, self).__init__(yaml)
    
    @raml_optional
    @raml_simple_parse
    def parse_displayName(self): pass
    
    @raml_optional
    @raml_simple_parse
    def parse_description(self): pass
    
    @raml_optional
    def parse_uriParameters(self): 
        self.uriParameters = {x[0] : RamlURIParameter(x[1]) for x in self.yaml['uriParameters'].iteritems()}
        
    @raml_optional
    def parse_baseUriParameters(self):
        self.baseUriParameters = {x[0] : RamlURIParameter(x[1]) for x in self.yaml['baseUriParameters'].iteritems()}
        
    @raml_optional
    def parse_get(self):
        self.get = None if 'get' not in self.yaml else RamlMethod(self.yaml['get'])
        self.methods['get'] = self.get
        
    @raml_optional
    def parse_post(self):
        self.post = None if 'post' not in self.yaml else RamlMethod(self.yaml['post'])
        self.methods['post'] = self.post
        
    @raml_optional
    def parse_put(self):
        self.put = None if 'put' not in self.yaml else RamlMethod(self.yaml['put'])
        self.methods['put'] = self.put
        
    @raml_optional
    def parse_delete(self):
        self.delete = None if 'delete' not in self.yaml else RamlMethod(self.yaml['delete'])
        self.methods['delete'] = self.delete

    
    def __str__(self):
        return \
'''[RamlResource({0.path},
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
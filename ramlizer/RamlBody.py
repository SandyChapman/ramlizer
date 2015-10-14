from .RamlParseable import RamlParseable
from .RamlizerParseError import RamlizerParseError
from .decorators import raml_optional, raml_tabbed
import json
import jsonschema


FORM_MIME_TYPES = (
    'application/x-www-form-urlencoded',
    'multipart/form-data',
)

JSON_MIME_TYPES = (
    'application/json',
    'application/hal+json',
)


class RamlBody(RamlParseable):

    def __init__(self, encoding, yaml):
        self.encoding = encoding
        super(RamlBody, self).__init__(yaml)

    def is_json_type(self):
        return self.encoding in JSON_MIME_TYPES

    def is_validatable(self):
        return self.is_json_type()

    def post_parse(self):
        if self.is_validatable() and self.example is not None:
            try:
                jsonschema.validate(self.example, self.schema)
                print('schema+example passed validation.')
            except jsonschema.exceptions.ValidationError as e:
                print(e)
                print('Skipping code generation.')

    @raml_optional
    def parse_schema(self):
        self.schema = self.yaml['schema']

    @raml_optional
    def parse_example(self):
        if self.is_json_type():
            self.example = json.loads(self.yaml['example'])
        else:
            self.example = self.yaml['example']

    @raml_optional
    def parse_formParameters(self):
        self.formParameters = self.yaml.get('formParameters', None)
        if self.encoding in FORM_MIME_TYPES and self.formParameters is None:
            raise RamlizerParseError(
                "Body\'s with encoding type {0} MUST specify the"
                " name-value pairs the API is expecting.".format(
                    self.encoding))

    @raml_tabbed
    def __str__(self):
        return '''\
[RamlBody({0.encoding})
    schema: {0.schema}
    example: {0.example}
    formParameters: {0.formParameters}
]'''.format(self)

    def __repr__(self):
        return str(self)

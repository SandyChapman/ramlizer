#!/usr/bin/python

from decorators import *
from RamlParseable import RamlParseable
from RamlBody import RamlBody
from RamlizerParseError import RamlizerParseError
from RamlResponse import RamlResponse

class RamlMethod(RamlParseable):

    def __init__(self, yaml):
        super(RamlMethod, self).__init__(yaml)
        
    @raml_optional
    @raml_simple_parse
    def parse_description(self): pass
    
    @raml_optional
    @raml_simple_parse
    def parse_headers(self): pass
    
    @raml_optional
    @raml_simple_parse
    def parse_protocols(self): pass
    
    @raml_optional
    @raml_simple_parse
    def parse_queryParameters(self): pass
    
    @raml_optional
    def parse_body(self):
        self.body = {body_encoding[0] : RamlBody(body_encoding[0], body_encoding[1]) for body_encoding in self.yaml['body'].iteritems()}
        
    @raml_optional
    def parse_responses(self):
        self.response = {response_code[0] : RamlResponse(response_code[0], response_code[1]) for response_code in self.yaml['responses'].iteritems()}
            
    @raml_tabbed
    def __str__(self):
        return \
'''[RamlMethod
    description: {0.description}
    headers: {0.headers}
    protocols: {0.protocols}
    queryParameters: {0.queryParameters}
    body: {0.body}
    response: {0.response}
]'''.format(self)
    
    

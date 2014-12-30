#!/usr/bin/python

from decorators import *
from RamlBody import RamlBody
from RamlParseable import RamlParseable

class RamlResponse(RamlParseable):

    def __init__(self, code, yaml):
        self.code = code
        super(RamlResponse, self).__init__(yaml)
        
    @raml_optional
    @raml_simple_parse
    def parse_description(self): pass
        
    @raml_optional
    @raml_simple_parse
    def parse_headers(self): pass
        
    @raml_optional
    def parse_body(self):
        self.body = {body_encoding[0] : RamlBody(body_encoding[0], body_encoding[1]) for body_encoding in self.yaml['body'].iteritems()}

    @raml_tabbed        
    def __str__(self):
        return \
'''[RamlResponse({0.code}):
    description: {0.description}
    headers: {0.headers}
    body: {0.body}
]'''.format(self)

    def __repr__(self):
        return str(self)
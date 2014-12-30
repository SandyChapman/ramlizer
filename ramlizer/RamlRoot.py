#!/usr/bin/python

from RamlParseable import RamlParseable
from RamlDocumentation import RamlDocumentation
from RamlResource import RamlResource
from RamlURIParameter import RamlURIParameter
from decorators import raml_required, raml_simple_parse, raml_optional, raml_tabbed
        
class RamlRoot(RamlParseable):

    def __init__(self, yaml):
        super(RamlRoot, self).__init__(yaml)
        
    @raml_required
    @raml_simple_parse
    def parse_title(self): pass
    
    @raml_optional
    @raml_simple_parse
    def parse_version(self): pass
        
    @raml_required
    @raml_simple_parse
    def parse_baseUri(self): pass
           
    @raml_optional
    def parse_baseUriParameters(self):
        self.baseUriParameters = {x[0] : RamlURIParameter(x[1]) for x in self.yaml['baseUriParameters'].iteritems()}
        
    @raml_optional
    @raml_simple_parse
    def parse_protocols(self): pass
        
    @raml_optional
    @raml_simple_parse
    def parse_mediaType(self): pass
    
    @raml_optional
    @raml_simple_parse
    def parse_schemas(self): pass
        
    @raml_optional
    def parse_uriParameters(self): 
        self.uriParameters = {x[0] : RamlURIParameter(x[1]) for x in self.yaml['uriParameters'].iteritems()}
        
    @raml_optional
    def parse_resources(self):
        self.resources = {x[0] : RamlResource(x[0], x[1]) for x in filter(lambda x: x[0].startswith('/'), self.yaml.iteritems())}
        
    @raml_optional
    def parse_documentation(self):
        self.documentation = RamlDocumentation(self.yaml['documentation'])
                
    @raml_tabbed
    def __str__(self):
        return \
'''[RamlRoot:
    title: {0.title}
    version: {0.version}
    base URI: {0.baseUri}
    base URI parameters: {0.baseUriParameters}
    protocols: {0.protocols}
    media type: {0.mediaType}
    URI parameters: {0.uriParameters}
    documentation:
        {0.documentation}
    schemas: {0.schemas}
    resources: {0.resources}
]'''.format(self)
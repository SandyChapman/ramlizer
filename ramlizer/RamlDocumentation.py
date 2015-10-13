#!/usr/bin/python
               
from .RamlParseable import RamlParseable
from .decorators import raml_required, raml_simple_parse, raml_optional, raml_tabbed

class RamlDocument(RamlParseable):

    def __init__(self, yaml):
        super(RamlDocument, self).__init__(yaml)
        
    @raml_required
    def parse_title(self):
        self.title = self.yaml['title']
        
    @raml_required
    def parse_content(self):
        self.content = self.yaml['content']
        
    @raml_tabbed
    def __str__(self):
        return \
'''[RamlDocument:
    title:{0.title}
    content:{0.content}
]'''.format(self)
        
    def __repr__(self):
        return '[RamlDocument:{0.title}]'.format(self)
        
class RamlDocumentation(RamlParseable):

    def __init__(self, yaml):
        super(RamlDocumentation, self).__init__(yaml)

    @raml_required
    def parse_documents(self):
        self.documents = [RamlDocument(document_yaml) for document_yaml in self.yaml]
    
    @raml_tabbed
    def __str__(self):
        return \
'''[RamlDocumentation:
    documents:
        {0.documents}
]'''.format(self)

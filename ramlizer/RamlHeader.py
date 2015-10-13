#!/usr/bin/python

from .RamlNamedParameter import RamlNamedParameter
from .decorators import *

class RamlHeader(RamlNamedParameter):
    
    def __init__(self, header_name, yaml):
        self.name = header_name
        super(RamlHeader, self).__init__(yaml)
            
    @raml_tabbed
    def __str__(self):
        return '[RamlHeader:\n    name:{0}{1}]'.format(self.name, super(RamlHeader, self).__str__())
        
    def __repr__(self):
        return str(self)

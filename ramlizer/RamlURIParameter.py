#!/usr/bin/python

from decorators import raml_optional, raml_required, raml_simple_parse, raml_enum_parse
from RamlParseable import RamlParseable
from RamlizerParseError import RamlizerParseError

class RamlNamedParameter(RamlParseable):

    def __init__(self, yaml):
        super(RamlNamedParameter, self).__init__(yaml)
    
    @raml_optional
    @raml_simple_parse
    def parse_displayName(self): pass
    
    @raml_optional
    @raml_simple_parse
    def parse_description(self): pass
    
    @raml_optional
    @raml_enum_parse('string', 'number', 'integer', 'date', 'boolean', 'file', default=0)
    def parse_type(self):
        try:
            if self.type != 'string':
                if self.enum != None:
                    raise RamlizerParseError('enum parameter can only be used with string type Named Parameters.')
                if self.pattern != None:
                    raise RamlizerParseError('pattern parameter can only be used with string type Named Parameters.')
                if self.minLength != None:
                    raise RamlizerParseError('minLength parameter can only be used with string type Named Parameters.')
                if self.maxLength != None:
                    raise RamlizerParseError('maxLength parameter can only be used with string type Named Parameters.')
            if self.type != 'integer':
                if self.minimum != None:
                    raise RamlizerParseError('minimum parameter can only be used with integer type Named Parameters.')
                if self.maximum != None:
                    raise RamlizerParseError('maximum parameter can only be used with integer type Named Parameters.!')
                
        except AttributeError as e:
            pass
    
    @raml_optional
    @raml_simple_parse
    def parse_enum(self):
        try:
            if self.enum != None and self.type != 'string':
                raise RamlizerParseError('RamlizerParseError!')
        except AttributeError as e:
            pass
            
    
    @raml_optional
    @raml_simple_parse
    def parse_pattern(self):
        #TODO: Validate pattern is a regex.
        try:
            if self.pattern != None and self.type != 'string':
                raise RamlizerParseError('RamlizerParseError!')
        except AttributeError as e:
            pass
    
    @raml_optional
    @raml_simple_parse
    def parse_minLength(self):
        try:
            if self.minLength != None and self.type != 'string':
                raise RamlizerParseError('RamlizerParseError!')
        except AttributeError as e:
            pass
    
    @raml_optional
    @raml_simple_parse
    def parse_maxLength(self): 
        try:
            if self.maxLength != None and self.type != 'string':
                raise RamlizerParseError('RamlizerParseError!')
        except AttributeError as e:
            pass
    
    @raml_optional
    @raml_simple_parse
    def parse_minimum(self): 
        try:
            if self.minimum != None and self.type != 'integer':
                raise RamlizerParseError('RamlizerParseError!')
        except AttributeError as e:
            pass
    
    @raml_optional
    @raml_simple_parse
    def parse_maximum(self): 
        try:
            if self.maximum != None and self.type != 'integer':
                raise RamlizerParseError('RamlizerParseError!')
        except AttributeError as e:
            pass
        
    @raml_optional
    @raml_simple_parse
    def parse_example(self): pass
        
    @raml_optional
    @raml_simple_parse
    def parse_repeat(self): pass
        
    @raml_optional
    @raml_simple_parse
    def parse_required(self): pass
        
    @raml_optional
    @raml_simple_parse
    def parse_default(self): pass
                
class RamlURIParameter(RamlNamedParameter):

    def __init__(self, yaml):
        super(RamlURIParameter, self).__init__(yaml)
            
    def __repr__(self):
        return '[RamlURIParameter: {0.type}]'.format(self)
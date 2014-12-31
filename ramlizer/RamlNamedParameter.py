#!/usr/bin/python

from RamlParseable import RamlParseable
from decorators import *

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
    
    def __str__(self):
        return \
'''
    displayName: {0.displayName}
    description: {0.description}
    type: {0.type}
    enum: {0.enum}
    pattern: {0.pattern}
    minLength: {0.minLength}
    maxLength: {0.maxLength}
    minimum: {0.minimum}
    maximum: {0.maximum}
    example: {0.example}
    repeat: {0.repeat}
    required: {0.required}
    default: {0.default}
'''.format(self)

    def __repr__(self):
        return '[RamlNamedParameter:\n{0}\n]'.format(str(self))
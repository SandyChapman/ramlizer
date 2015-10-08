#!/usr/bin/python

from .RamlizerParseError import RamlizerParseError
   
def raml_required(func):
    def check_required(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyError as e:
            class_name = args[0].__class__.__name__
            function_name = func.__name__
            raise RamlizerParseError('Failed parsing. Required parameter missing in {0}::{1}.'.format(class_name, function_name))
    return check_required
    
def raml_optional(func):
    def check_optional(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyError as e:
            setattr(args[0], e.args[0], None) # Ignore optional parse failures. Set value to None.
    return check_optional
    
def raml_tabbed(func):
    def tab(*args, **kwargs):
        return func(*args, **kwargs).replace('\n', '\n\t')
    return tab

def raml_simple_parse(func):
    def parse(*args, **kwargs):
        self = args[0]
        attribute = func.__name__.replace('parse_', '')
        value = self.yaml[attribute]
        setattr(self, attribute, value)
        func(*args, **kwargs)
    return parse
        
class raml_enum_parse(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self, func):
        def validate_enum(*args, **kwargs):
            raml_self = args[0]
            attribute = func.__name__.replace('parse_', '')
            if 'default' in self.kwargs:
                value = raml_self.yaml.get(attribute, self.args[self.kwargs['default']])
            else:
                value = raml_self.yaml[attribute]
            if value not in self.args:
                class_name = args[0].__class__.__name__
                function_name = func.__name__
                raise RamlizerParseError('Failed parsing. Parameter not in allowable enum range {0}::{1}.'.format(class_name, function_name))
            setattr(raml_self, attribute, value)
            func(*args, **kwargs)
        return validate_enum

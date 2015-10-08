from .RamlParseable import RamlParseable
from .RamlizerParseError import RamlizerParseError
from .decorators import raml_optional, raml_enum_parse, raml_simple_parse


def only_with(what, used_with):
    raise RamlizerParseError(
        '%s can only be used with %s type Named Parameters.'
        % (what, used_with))


class RamlNamedParameter(RamlParseable):

    def __init__(self, yaml):
        super(RamlNamedParameter, self).__init__(yaml)

    @raml_optional
    @raml_simple_parse
    def parse_displayName(self):
        pass

    @raml_optional
    @raml_simple_parse
    def parse_description(self):
        pass

    @raml_optional
    @raml_enum_parse('string', 'number', 'integer', 'date', 'boolean', 'file',
                     default=0)
    def parse_type(self):
        try:
            if self.type != 'string':
                if self.enum is not None:
                    only_with('enum', 'string')
                if self.pattern is not None:
                    only_with('pattern', 'string')
                if self.minLength is not None:
                    only_with('minLength', 'string')
                if self.maxLength is not None:
                    only_with('maxLength', 'string')
            if self.type != 'integer':
                if self.minimum is not None:
                    only_with('minimum', 'integer')
                if self.maximum is not None:
                    only_with('maximum', 'integer')
        except AttributeError:
            pass

    @raml_optional
    @raml_simple_parse
    def parse_enum(self):
        try:
            if self.enum is not None and self.type != 'string':
                raise RamlizerParseError('RamlizerParseError!')
        except AttributeError:
            pass

    @raml_optional
    @raml_simple_parse
    def parse_pattern(self):
        # TODO: Validate pattern is a regex.
        try:
            if self.pattern is not None and self.type != 'string':
                raise RamlizerParseError('RamlizerParseError!')
        except AttributeError:
            pass

    @raml_optional
    @raml_simple_parse
    def parse_minLength(self):
        try:
            if self.minLength is not None and self.type != 'string':
                raise RamlizerParseError('RamlizerParseError!')
        except AttributeError:
            pass

    @raml_optional
    @raml_simple_parse
    def parse_maxLength(self):
        try:
            if self.maxLength is not None and self.type != 'string':
                raise RamlizerParseError('RamlizerParseError!')
        except AttributeError:
            pass

    @raml_optional
    @raml_simple_parse
    def parse_minimum(self):
        try:
            if self.minimum is not None and self.type != 'integer':
                raise RamlizerParseError('RamlizerParseError!')
        except AttributeError:
            pass

    @raml_optional
    @raml_simple_parse
    def parse_maximum(self):
        try:
            if self.maximum is not None and self.type != 'integer':
                raise RamlizerParseError('RamlizerParseError!')
        except AttributeError:
            pass

    @raml_optional
    @raml_simple_parse
    def parse_example(self):
        pass

    @raml_optional
    @raml_simple_parse
    def parse_repeat(self):
        pass

    @raml_optional
    @raml_simple_parse
    def parse_required(self):
        pass

    @raml_optional
    @raml_simple_parse
    def parse_default(self):
        pass

    def __str__(self):
        return '''\
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

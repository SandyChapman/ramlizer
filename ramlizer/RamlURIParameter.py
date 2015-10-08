from .decorators import raml_tabbed
from .RamlNamedParameter import RamlNamedParameter


class RamlURIParameter(RamlNamedParameter):

    def __init__(self, yaml):
        super(RamlURIParameter, self).__init__(yaml)

    @raml_tabbed
    def __str__(self):
        return '[RamlURIParameter:{0}]'.format(
            super(RamlURIParameter, self).__str__())

    def __repr__(self):
        return str(self)

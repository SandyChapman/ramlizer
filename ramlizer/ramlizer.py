#!/usr/bin/env python

import yaml
from RamlRoot import RamlRoot
import os.path

# \see http://stackoverflow.com/a/9577670/1270148
class RamlIncludeLoader(yaml.Loader):

    def __init__(self, stream):
        self._root = os.path.split(stream.name)[0]
        super(RamlIncludeLoader, self).__init__(stream)

    def include(self, node):
        filename = os.path.join(self._root, self.construct_scalar(node))
        with open(filename, 'r') as f:
            return yaml.load(f, RamlIncludeLoader)

RamlIncludeLoader.add_constructor('!include', RamlIncludeLoader.include)

class RamlFile():
    
    def __init__(self, read_file):
        self.yaml = yaml.load(read_file)
        self.parse()
        
    def parse(self):
        self.root = RamlRoot(self.yaml)
        
    def __str__(self):
        return \
'''[RamlFile:
    {0}
]'''.format(self.root)

#!/usr/bin/env python

import yaml
from RamlRoot import RamlRoot

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

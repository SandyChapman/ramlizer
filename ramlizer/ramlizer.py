import os.path
import yaml
from .RamlRoot import RamlRoot


class RamlFile():
    def __init__(self, read_file):
        class Loader(yaml.Loader):
            def __init__(self, stream):
                self._root = os.path.split(stream.name)[0]
                super(Loader, self).__init__(stream)

            def include(self, node):
                filename = os.path.join(self._root,
                                        self.construct_scalar(node))
                with open(filename, 'r') as f:
                    return yaml.load(f, Loader)
        yaml.add_constructor('!include', Loader.include)

        self.yaml = yaml.load(read_file, Loader)
        self.parse()

    def parse(self):
        self.root = RamlRoot(self.yaml)

    def __str__(self):
        return '[RamlFile:\n    {0}]'.format(self.root)

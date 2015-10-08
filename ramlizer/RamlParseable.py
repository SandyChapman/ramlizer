class RamlParseable(object):

    def __init__(self, yaml):
        self.yaml = yaml
        self.parse()

    def parse(self):
        for method in dir(self):
            if not method.startswith('parse_'):
                continue
            getattr(self, method)()
        if 'post_parse' in dir(self):
            self.post_parse()

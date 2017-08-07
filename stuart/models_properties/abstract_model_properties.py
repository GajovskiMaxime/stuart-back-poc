
class AbstractModelProperties(object):

    def __init__(self, properties):
        self.__properties = properties
        for key, value in self.get_columns().items():
            value['name'] = key.upper()

    def get_column(self, key):
        return self.__properties['columns'][key]

    def get_relation(self, key):
        return self.__properties['relationships'][key]

    def get_columns(self):
        return self.__properties['columns']

    def get_relations(self):
        return self.__properties['relationships']

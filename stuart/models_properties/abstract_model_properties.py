
class AbstractModelProperties(object):

    def __init__(self, properties):
        self.__properties = properties
        for key, value in self.get_columns().items():
            value['name'] = key.upper()

        mandatory_fields = []
        for k_column, v_column in self.get_columns().items():
            if 'nullable' in v_column \
                    and v_column['nullable'] is False\
                    and 'default' not in v_column:
                mandatory_fields.append(k_column)
        self.__properties['mandatory_fields'] = mandatory_fields

    def get_mandatory_fields(self):
        return self.__properties['mandatory_fields']

    def get_column(self, key):
        return self.__properties['columns'][key]

    def get_relation(self, key):
        return self.__properties['relationships'][key]

    def get_columns(self):
        return self.__properties['columns']

    def get_relations(self):
        return self.__properties['relationships']

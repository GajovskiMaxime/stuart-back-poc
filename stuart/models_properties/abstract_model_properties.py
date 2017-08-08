
class AbstractModelProperties(object):

    def __init__(self, properties):
        self.__properties = properties
        for key, value in self.get_columns().items():
            value['sql']['name'] = key.upper()

        mandatory_keys = []
        for k_column, v_column in self.get_columns().items():
            if 'nullable' in v_column['sql'] \
                    and v_column['sql']['nullable'] is False\
                    and 'default' not in v_column['sql']:
                mandatory_keys.append(k_column)
        self.__properties['mandatory_keys'] = mandatory_keys

    def get_mandatory_keys(self):
        return self.__properties['mandatory_keys']

    def get_sql_attr_column(self, key):
        return self.__properties['columns'][key]['sql']

    def get_json_attr_column(self, key):
        return self.__properties['columns'][key]['json']

    def get_column(self, key):
        return self.__properties['columns'][key]

    def get_relation(self, key):
        return self.__properties['relationships'][key]

    def get_columns(self):
        return self.__properties['columns']

    def get_relations(self):
        return self.__properties['relationships']

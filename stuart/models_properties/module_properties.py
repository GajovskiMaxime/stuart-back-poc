from sqlalchemy import Integer, String, Boolean

from stuart.models_properties.abstract_model_properties import AbstractModelProperties


class ModuleProperties(AbstractModelProperties):

    __properties = {
        'columns': {
            'id': {
                'type_': Integer,
                'primary_key': True
            },
            'label': {
                'type_': String,
                'nullable': False
            },
            'command': {
                'type_': String,
                'nullable': False
            },
            'is_preset': {
                'type_': Boolean,
                'nullable': False,
                'default': False
            },
        },
        'relationships': {
            'actions': {
                'argument': 'Action',
                'lazy': 'joined',
                'cascade': 'save-update, merge, delete'
            }
        }
    }

    def __init__(self):
        super(ModuleProperties, self).__init__(self.__properties)

    def get_column(self, key):
        return super(ModuleProperties, self).get_column(key)

    def get_relation(self, key):
        return super(ModuleProperties, self).get_relation(key)

    def get_columns(self):
        return super(ModuleProperties, self).get_columns()

    def get_relations(self):
        return super(ModuleProperties, self).get_relations()

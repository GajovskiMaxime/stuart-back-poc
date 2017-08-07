from sqlalchemy import Integer, String, Boolean

from stuart.models_properties.abstract_model_properties import AbstractModelProperties


class ActionProperties(AbstractModelProperties):

    __properties = {
        'columns': {
            'id': {
                'type_': Integer,
                'primary_key': True
            },
            'module_id': {
                'type_': Integer,
                'nullable': False
            },
            'category': {
                'type_': String,
                'nullable': True
            },
            'label': {
                'type_': String,
                'nullable': False
            },
            'command': {
                'type_': String,
                'nullable': False
            },
            'is_tested': {
                'type_': Boolean,
                'nullable': True,
                'default': False
            },
            'is_preset': {
                'type_': Boolean,
                'nullable': False
            }
        },
        'relationships': {

        }
    }

    def __init__(self):
        super(ActionProperties, self).__init__(self.__properties)

    def get_column(self,  key):
        return super(ActionProperties, self).get_column(key)

    def get_relation(self, key):
        return super(ActionProperties, self).get_relation(key)

    def get_columns(self):
        return super(ActionProperties, self).get_columns()

    def get_relations(self):
        return super(ActionProperties, self).get_relations()

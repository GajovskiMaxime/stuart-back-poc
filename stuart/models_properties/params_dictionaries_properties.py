from sqlalchemy import Integer, String

from stuart.models_properties.abstract_model_properties import AbstractModelProperties


class ParamsDictionariesProperties(AbstractModelProperties):

    __properties = {
        'columns': {
            'id': {
                'type_': Integer,
                'primary_key': True
            },
            'args_map': {
                'type_': String,
                'nullable': False
            },
            'target_map': {
                'type_': String,
                'nullable': False
            }
        },
        'relationships': {

        }
    }

    def __init__(self):
        super(ParamsDictionariesProperties, self).__init__(self.__properties)

    def get_column(self, key):
        return super(ParamsDictionariesProperties, self).get_column(key)

    def get_relation(self, key):
        return super(ParamsDictionariesProperties, self).get_relation(key)

    def get_columns(self):
        return super(ParamsDictionariesProperties, self).get_columns()

    def get_relations(self):
        return super(ParamsDictionariesProperties, self).get_relations()

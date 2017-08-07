from sqlalchemy import Integer, String

from stuart.models_properties.model_properties import ModelProperties

from stuart.models_properties.abstract_model_properties import AbstractModelProperties


class GenericParamsPatternsProperties(AbstractModelProperties):

    __properties = {
        'columns': {
            'id': {
                'type_': Integer,
                'primary_key': True
            },
            'generic_args_pattern': {
                'type_': String,
                'nullable': False
            },
            'generic_target_pattern': {
                'type_': String,
                'nullable': False
            }
        },
        'relationships': {

        }
    }

    def __init__(self):
        super(GenericParamsPatternsProperties, self).__init__(self.__properties)

    def get_column(self, key):
        return super(GenericParamsPatternsProperties, self).get_column(key)

    def get_relation(self, key):
        return super(GenericParamsPatternsProperties, self).get_relation(key)

    def get_columns(self):
        return super(GenericParamsPatternsProperties, self).get_columns()

    def get_relations(self):
        return super(GenericParamsPatternsProperties, self).get_relations()

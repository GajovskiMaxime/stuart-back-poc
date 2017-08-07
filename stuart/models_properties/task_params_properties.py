from sqlalchemy import Integer

from stuart.models_properties.model_properties import ModelProperties

from stuart.models_properties.abstract_model_properties import AbstractModelProperties


class TaskParamsProperties(AbstractModelProperties):

    __properties = {
        'columns': {
            'id': {
                'type_': Integer,
                'primary_key': True
            },
            'params_patterns_id': {
                'type_': Integer,
                'nullable': False
            },
            'params_dictionaries_id': {
                'type_': Integer,
                'nullable': False
            },
        },
        'relationships': {
            'params_patterns': {
                'argument': 'ParamsPatterns',
                'lazy': 'subquery',
                'cascade': 'save-update, merge, delete'
            },
            'params_dictionaries': {
                'argument': 'ParamsDictionaries',
                'lazy': 'subquery',
                'cascade': 'save-update, merge, delete'
            }
        }
    }

    def __init__(self):
        super(TaskParamsProperties, self).__init__(self.__properties)

    def get_column(self, key):
        return super(TaskParamsProperties, self).get_column(key)

    def get_relation(self, key):
        return super(TaskParamsProperties, self).get_relation(key)

    def get_columns(self):
        return super(TaskParamsProperties, self).get_columns()

    def get_relations(self):
        return super(TaskParamsProperties, self).get_relations()

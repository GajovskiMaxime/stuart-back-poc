from sqlalchemy import Integer

from stuart.models_properties.abstract_model_properties import AbstractModelProperties


class TaskParamsProperties(AbstractModelProperties):

    __properties = {
        'columns': {
            'id': {
                'sql': {
                    'type_': Integer,
                    'primary_key': True
                }
            },
            'params_patterns_id': {
                'sql': {
                    'type_': Integer,
                    'nullable': False
                },
                'json': {
                    'object_expected': True
                }
            },
            'params_dictionaries_id': {
                'sql': {
                    'type_': Integer,
                    'nullable': False
                },
                'json': {
                    'object_expected': True
                }
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
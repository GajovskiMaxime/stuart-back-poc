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
            'generic_params_patterns': {
                'sql': {
                    'type_': Integer,
                    'nullable': False
                },
                'json': {
                    'expected_type': 'json_object'
                }
            },
            'params_dictionaries': {
                'sql': {
                    'type_': Integer,
                    'nullable': False
                },
                'json': {
                    'expected_type': 'json_object'
                }
            },
        },
        'relationships': {
            'generic_params_patterns': {
                'argument': 'GenericParamsPatterns',
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
        super(TaskParamsProperties, self).__init__(
            self.__properties)

from datetime import datetime

from sqlalchemy import Integer, DateTime

from stuart.models_properties.abstract_model_properties import AbstractModelProperties


class UserTaskProperties(AbstractModelProperties):

    __properties = {
        'columns': {
            'id': {
                'sql': {
                    'type_': Integer,
                    'primary_key': True
                }
            },
            'task': {
                'sql': {
                    'type_': Integer,
                    'nullable': False
                },
                'json': {
                    'expected_type': 'id'
                }
            },
            'params_dictionaries': {
                'sql': {
                    'type_': Integer,
                    'nullable': False
                },
                'json': {
                    'expected_type': 'object'
                }
            },
            'created_at': {
                'sql': {
                    'type_': DateTime,
                    'nullable': False,
                    'default': datetime.now()
                },
                'json': {
                    'expected_type': 'field'
                }
            }
        },
        'relationships': {
            'params_dictionaries': {
                'argument': 'ParamsDictionaries',
                'lazy': 'subquery',
                'cascade': 'save-update, merge, delete'
            },
            'task': {
                'argument': 'Task',
                'lazy': 'subquery',
                'cascade': 'save-update, merge, delete'
            }
        }
    }

    def __init__(self):
        super(UserTaskProperties, self).__init__(
            self.__properties)

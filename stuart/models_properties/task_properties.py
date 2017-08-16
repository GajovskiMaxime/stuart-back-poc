from datetime import datetime

from sqlalchemy import Integer, String, DateTime

from stuart.models_properties.abstract_model_properties import AbstractModelProperties


class TaskProperties(AbstractModelProperties):

    __properties = {
        'columns': {
            'id': {
                'sql': {
                    'type_': Integer,
                    'primary_key': True
                }
            },
            'action': {
                'sql': {
                    'type_': Integer,
                    'nullable': False
                },
                'json': {
                    'expected_type': 'id'
                }
            },
            'custom_label': {
                'sql': {
                    'type_': String,
                    'nullable': True
                },
                'json': {
                    'expected_type': 'field'
                }
            },
            'task_params': {
                'sql': {
                    'type_': Integer,
                    'nullable': False
                },
                'json': {
                    'expected_type': 'json_object'
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
            },
        },
        'relationships': {
            'task_params': {
                'argument': 'TaskParams',
                'lazy': 'joined',
                'cascade': 'save-update, merge, delete'
            },
            'action': {
                'argument': 'Action',
                'lazy': 'subquery',
                'cascade': 'save-update, merge, delete'
            }
        }
    }

    def __init__(self):
        super(TaskProperties, self).__init__(
            self.__properties)

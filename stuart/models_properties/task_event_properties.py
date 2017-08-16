from datetime import datetime

from sqlalchemy import Integer, DateTime, String

from stuart.models_properties.abstract_model_properties import AbstractModelProperties


class TaskEventProperties(AbstractModelProperties):

    __properties = {
        'columns': {
            'id': {
                'sql': {
                    'type_': Integer,
                    'primary_key': True
                }
            },
            'user_task': {
                'sql': {
                    'type_': Integer,
                    'nullable': False
                },
                'json': {
                    'expected_type': 'id'
                }
            },
            'begin': {
                'sql': {
                    'type_': DateTime,
                    'nullable': False,
                    'default': datetime.now()
                },
                'json': {
                    'expected_type': 'field'
                }
            },
            "end": {
                'sql': {
                    'type_': DateTime,
                    'nullable': True
                },
                'json': {
                    'expected_type': 'field'
                }
            },
            "status": {
                'sql': {
                    'type_': String,
                    'nullable': True
                },
                'json': {
                    'expected_type': 'field'
                }
            }
        },
        'relationships': {
            'user_task': {
                'argument': 'UserTask',
                'lazy': 'subquery',
                'cascade': 'save-update, merge, delete'
            }
        }
    }

    def __init__(self):
        super(TaskEventProperties, self).__init__(
            self.__properties)

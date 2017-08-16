
from sqlalchemy import Integer, String

from stuart.models_properties.abstract_model_properties import AbstractModelProperties


class LogEventProperties(AbstractModelProperties):

    __properties = {
        'columns': {
            'id': {
                'sql': {
                    'type_': Integer,
                    'primary_key': True
                }
            },
            'task_event': {
                'sql': {
                    'type_': Integer,
                    'nullable': False
                },
                'json': {
                    'expected_type': 'id'
                }
            },
            'status_code': {
                'sql': {
                    'type_': String,
                    'nullable': True
                },
                'json': {
                    'expected_type': 'field'
                }
            },
            "stdout": {
                'sql': {
                    'type_': String,
                    'nullable': True
                },
                'json': {
                    'expected_type': 'field'
                }
            },
            "stderr": {
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
            'task_event': {
                'argument': 'TaskEvent',
                'lazy': 'subquery',
                'cascade': 'save-update, merge, delete'
            }
        }
    }

    def __init__(self):
        super(LogEventProperties, self).__init__(
            self.__properties)

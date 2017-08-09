from sqlalchemy import Integer, String, Boolean

from stuart.models_properties.abstract_model_properties import AbstractModelProperties


class ActionProperties(AbstractModelProperties):

    __properties = {
        'columns': {
            'id': {
                'sql': {
                    'type_': Integer,
                    'primary_key': True
                }
            },
            'module': {
                'sql': {
                    'type_': Integer,
                    'nullable': False
                },
                'json': {
                    'expected_type': 'id'
                }
            },
            'category': {
                'sql': {
                    'type_': String,
                    'nullable': True
                },
                'json': {
                    'expected_type': 'field'
                }
            },
            'label': {
                'sql': {
                    'type_': String,
                    'nullable': False
                },
                'json': {
                    'expected_type': 'field'
                }
            },
            'command': {
                'sql': {
                    'type_': String,
                    'nullable': False
                },
                'json': {
                    'expected_type': 'field'
                }
            },
            'is_tested': {
                'sql': {
                    'type_': Boolean,
                    'nullable': True,
                    'default': False
                },
                'json': {
                    'expected_type': 'field'
                }
            },
            'is_preset': {
                'sql': {
                    'type_': Boolean,
                    'nullable': False,
                    'default': False
                }
            }
        },
        'relationships': {
            'module': {
                'argument': 'Module'
            }
        }
    }

    def __init__(self):
        super(ActionProperties, self).__init__(
            self.__properties)

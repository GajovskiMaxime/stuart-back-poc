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
            'module_id': {
                'sql': {
                    'type_': Integer,
                    'nullable': False
                }
            },
            'category': {
                'sql': {
                    'type_': String,
                    'nullable': True
                }
            },
            'label': {
                'sql': {
                    'type_': String,
                    'nullable': False
                }
            },
            'command': {
                'sql': {
                    'type_': String,
                    'nullable': False
                }
            },
            'is_tested': {
                'sql': {
                    'type_': Boolean,
                    'nullable': True,
                    'default': False
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
        }
    }

    def __init__(self):
        super(ActionProperties, self).__init__(self.__properties)

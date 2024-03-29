from sqlalchemy import Integer, String, Boolean

from stuart.models_properties.abstract_model_properties import AbstractModelProperties


class ModuleProperties(AbstractModelProperties):

    __properties = {

        'columns': {
            'id': {
                'sql': {
                    'type_': Integer,
                    'primary_key': True
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
            'is_preset': {
                'sql': {
                    'type_': Boolean,
                    'nullable': False,
                    'default': False
                },
                'json': {
                    'expected_type': 'field'
                }
            },
        },
        'relationships': {
            'action_list': {
                'argument': 'Action',
                'lazy': 'joined',
                'cascade': 'save-update, merge, delete'
            }
        }
    }

    def __init__(self):
        super(ModuleProperties, self).__init__(
            self.__properties)

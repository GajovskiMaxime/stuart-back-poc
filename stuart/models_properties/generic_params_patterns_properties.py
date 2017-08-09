from sqlalchemy import Integer, String

from stuart.models_properties.abstract_model_properties import AbstractModelProperties


class GenericParamsPatternsProperties(AbstractModelProperties):

    __properties = {
        'columns': {
            'id': {
                'sql': {
                    'type_': Integer,
                    'primary_key': True
                }
            },
            'generic_args_pattern': {
                'sql': {
                    'type_': String,
                    'nullable': False
                },
                'json': {
                    'expected_type': 'field'
                }
            },
            'generic_target_pattern': {
                'sql': {
                    'type_': String,
                    'nullable': False
                },
                'json': {
                    'expected_type': 'field'
                }
            }
        },
        'relationships': {
        }
    }

    def __init__(self):
        super(GenericParamsPatternsProperties, self).__init__(
            self.__properties)

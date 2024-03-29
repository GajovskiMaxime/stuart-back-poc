from sqlalchemy import Integer, String

from stuart.models_properties.abstract_model_properties import AbstractModelProperties


class ParamsDictionariesProperties(AbstractModelProperties):

    __properties = {

        'columns': {
            'id': {
                'sql': {
                    'type_': Integer,
                    'primary_key': True
                }
            },
            'args_dictionary': {
                'sql': {
                    'type_': String,
                    'nullable': False
                },
                'json': {
                    'expected_type': 'json_string'
                }
            },
            'target_dictionary': {
                'sql': {
                    'type_': String,
                    'nullable': False
                },
                'json': {
                    'expected_type': 'json_string'
                }
            }
        },
        'relationships': {
        }
    }

    def __init__(self):
        super(ParamsDictionariesProperties, self).__init__(
            self.__properties)

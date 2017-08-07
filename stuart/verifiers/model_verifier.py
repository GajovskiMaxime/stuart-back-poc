from flask import current_app
from sqlalchemy import String

from stuart.exceptions.attribute.attribute_exception import AttributeException
from stuart.exceptions.attribute.attribute_not_found_exception import AttributeNotFoundException
from stuart.exceptions.attribute.empty_attribute_exception import EmptyAttributeException
from stuart.exceptions.attribute.unexpected_attribute_exception import UnexpectedAttributeException


class ModelVerifier(object):

    def __init__(self, table):
        super(ModelVerifier, self).__init__()
        self._table = table

    def verify_mandatory_fields(self, **args):
        mandatory_fields = self._table.mandatory_fields()
        for k_column, v_column in mandatory_fields.items():
            if k_column not in args:
                raise AttributeNotFoundException(
                    needed_attributes=k_column,
                    table=self._table)

    def verify_empty_fields(self, **args):
        mandatory_fields = self._table.mandatory_fields()
        for k_column, v_column in mandatory_fields.items():
                if v_column['type_'] == String:
                    if k_column in args and not args[k_column].strip():
                        raise EmptyAttributeException(
                            table=self._table,
                            attribute=k_column)

    def verify_extra_fields(self, **args):
        for k_column, v_column in args.items():
            if k_column in self._table.properties().get_relations():
                args.pop(k_column, None)

            if not hasattr(self._table, k_column):
                raise UnexpectedAttributeException(
                    unexpected_key=k_column,
                    unexpected_value=v_column)
        return args

    def verify_args(self, **args):
        try:
            self.verify_mandatory_fields(
                **args)

            return self.verify_extra_fields(
                **args)

        #     self.verify_empty_fields(
        #         table=self._table,
        #         **args)
        except AttributeException:
            raise

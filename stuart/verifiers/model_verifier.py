import sys
from simplejson import JSONDecodeError

from flask import json
from sqlalchemy import String

from stuart.exceptions.attribute.attribute_exception import AttributeException
from stuart.exceptions.attribute.attribute_not_found_exception import AttributeNotFoundException
from stuart.exceptions.attribute.empty_attribute_exception import EmptyAttributeException
from stuart.exceptions.database.database_exception import DatabaseException
from stuart.exceptions.database.unique_constraint_exception import UniqueConstraintException
from stuart.exceptions.json.double_quote_enclosure_exception import DoubleQuoteEnclosureException
from stuart.exceptions.json.malformed_json_exception import MalformedJSONObjectException


class ModelVerifier(object):

    def __init__(self, table):
        super(ModelVerifier, self).__init__()
        self._table = table

    def verify_mandatory_keys(self, **args):
        mandatory_fields = self._table.properties().get_mandatory_keys()
        for item in mandatory_fields:
            if item not in args:
                raise AttributeNotFoundException(
                    needed_attributes=item,
                    table=self._table)

    def verify_empty_fields(self, **args):
        mandatory_fields = self._table.properties().get_mandatory_keys()
        for item in mandatory_fields:
                if self._table.properties().get_sql_attr_column(item)['type_'] == String:
                    if item in args and not args[item].strip():
                        raise EmptyAttributeException(
                            table=self._table,
                            attribute=item)

    # def verify_extra_fields(self, **args):
    #     copy_args = args
    #     for k_column, v_column in args.items():
    #         if k_column in self._table.properties().get_relations():
    #             copy_args.pop(k_column, None)
    #
    #         if not hasattr(self._table, k_column):
    #             raise UnexpectedAttributeException(
    #                 unexpected_key=k_column,
    #                 unexpected_value=v_column)
    #     return copy_args

    def verify_values_with_recursion(self, session, autocommit, **args):
        for k, v in args.items():
            try:
                json_type = self._table.properties().get_json_attr_column(k)['expected_type']
                if json_type == 'json_string':
                    try:
                        json.loads(v)
                    except JSONDecodeError as json_err:
                        if 'Expecting value' in json_err.args[0]:
                            raise MalformedJSONObjectException(
                                key=k,
                                value=v)
                        if 'Expecting property name enclosed in double quotes' in json_err.args[0]:
                            raise DoubleQuoteEnclosureException(
                                value=v)
                elif json_type == 'field':
                    pass
                else:
                    class_name = self._table.properties().get_relation(k)['argument']
                    service_class = str(class_name + 'Service')
                    service = getattr(sys.modules['stuart.services'], service_class)()
                    if json_type == 'id':
                        try:
                            service.read(
                                filters={'id': v},
                                mode='exact')
                        except DatabaseException:
                            raise

                    elif json_type == 'object':
                        created_object = service.create_with_recursion(
                            args=v,
                            session=session,
                            autocommit=autocommit)
                        args[k] = created_object.id

            except UniqueConstraintException as err:
                args[k] = err.object_id

        return args

    def verify(self, autocommit, session, args):
        try:

            self.verify_mandatory_keys(**args)
            verified_args = self.verify_values_with_recursion(
                session=session,
                autocommit=autocommit,
                **args)

            # self.verify_extra_fields(
            #     **args)

            #     self.verify_empty_fields(
            #         table=self._table,
            #         **args)

            return verified_args

        except AttributeException:
            raise

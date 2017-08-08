import sys
from sqlalchemy import String
from stuart.exceptions.attribute.attribute_exception import AttributeException
from stuart.exceptions.attribute.attribute_not_found_exception import AttributeNotFoundException
from stuart.exceptions.attribute.empty_attribute_exception import EmptyAttributeException


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

    # TODO : Need to use service instead of DAO (for control)
    # TODO : Need to find a solution with session.commit (shared session)
    def verify_values(self, session, **args):
        for k, v in args.items():
            if self._table.properties().get_json_attr_column(k)['expected_type'] == 'object':
                class_name = self._table.properties().get_relation(k)['argument']
                dao_class = str(class_name + 'DAO')
                dao = getattr(sys.modules['stuart.dao'], dao_class)()
                created_object = dao.create(
                    session=session,
                    args=v)
                args[k] = created_object.id
        return args

    def verify(self, session, args):
        try:
            self.verify_mandatory_keys(**args)
            verified_args = self.verify_values(session, **args)

            # self.verify_extra_fields(
            #     **args)

            #     self.verify_empty_fields(
            #         table=self._table,
            #         **args)

            return verified_args

        except AttributeException:
            raise

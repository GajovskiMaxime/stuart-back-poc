from flask import current_app

from stuart.exceptions.database.object_not_found_exception import ObjectNotFoundException


class AbstractGenericDAO(object):

    def __init__(self, table):
        super(AbstractGenericDAO, self).__init__()
        self._table = table

    def create(self, session, model):
        session.add(model)
        return model

    def read_by_id(self, session, object_id):
        return AbstractGenericDAO.__read_by_id(
            session=session,
            table=self._table,
            object_id=object_id)

    @staticmethod
    def __read_by_id(session, table, object_id):
        object_to_get = session.query(table).get(object_id)
        if object_to_get is None:
            raise ObjectNotFoundException(
                object_id=object_id,
                table=table)
        return object_to_get

    @property
    def table(self):
        return self._table

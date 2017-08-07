from flask import current_app
from sqlalchemy import Integer, String, Boolean

from stuart.exceptions.database.empty_table_exception import EmptyTableException
from stuart.exceptions.database.filter_exception import FilterException
from stuart.exceptions.database.object_not_found_exception import ObjectNotFoundException
from stuart.exceptions.database.preset_exception import PresetException


class AbstractGenericDAO(object):

    def __init__(self, table):
        super(AbstractGenericDAO, self).__init__()
        self._table = table

    def create(self, session, model):
        session.add(model)
        return model

    def __get_objects_with_filters(self, query, filters):
        try:

            for k, v in filters.items():
                if not v or v is None:
                    query = query.filter(self._table.__getattribute__(self._table, k).is_(None))

                elif self._table.properties().get_column(k)['type_'] is Boolean:
                    v = True if v.lower() == 'true' else False
                    query = query.filter(self._table.__getattribute__(self._table, k).is_(v))

                elif self._table.properties().get_column(k)['type_'] is String:
                    query = query.filter(self._table.__getattribute__(self._table, k).ilike('%' + v + '%'))

                if self._table.properties().get_column(k)['type_'] is Integer:
                    query = query.filter(self._table.__getattribute__(self._table, k) == int(v))
        except ValueError:
            raise FilterException(
                filters=filters)
        return query.all()

    def read_all(self, session, filters):
        objects = self.__get_objects_with_filters(
            query=session.query(self._table),
            filters=filters)

        if not objects:
            if len(filters) != 0:
                raise ObjectNotFoundException(
                    filters=filters,
                    table=self._table)
            raise EmptyTableException(
                table=self._table)

        return objects

    def delete(self, session, filters):
        try:
            object_from_db = self.read_all(
                session=session,
                filters=filters)[0]

            if object_from_db.is_preset:
                raise PresetException(
                    object_id=filters['id'],
                    table=self._table,
                    action='delete')

            session.delete(object_from_db)
        except ObjectNotFoundException:
            raise
        return filters['id']

    @property
    def table(self):
        return self._table

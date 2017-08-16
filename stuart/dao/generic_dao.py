from flask import current_app
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.exc import OperationalError

from stuart.exceptions.database.filter_exception import FilterException
from stuart.exceptions.database.object_not_found_exception import ObjectNotFoundException
from stuart.exceptions.database.preset_exception import PresetException
from stuart.exceptions.database.table_not_found_exception import TableNotFoundException


class GenericDAO(object):

    def __init__(self, table):
        super(GenericDAO, self).__init__()
        self._table = table

    def create(self, session, args):
        model = self._table(**args)
        session.add(model)
        session.flush()
        return model

    def __get_objects_with_filters(self, query, mode, filters):
        try:
            for k, v in filters.items():
                if v is None:
                    query = query.filter(self._table.__getattribute__(self._table, k).is_(None))
                elif self._table.properties().get_sql_attr_column(k)['type_'] is Boolean:
                    query = query.filter(self._table.__getattribute__(self._table, k).is_(v))
                elif self._table.properties().get_sql_attr_column(k)['type_'] is String:
                    if mode == 'contains':
                        query = query.filter(self._table.__getattribute__(self._table, k).ilike('%' + v + '%'))
                    if mode == 'exact':
                        query = query.filter(self._table.__getattribute__(self._table, k) == str(v))
                if self._table.properties().get_sql_attr_column(k)['type_'] is Integer:
                    query = query.filter(self._table.__getattribute__(self._table, k) == int(v))

            return query.all()

        except (ValueError, KeyError):
            raise FilterException(
                filters=filters)
        except OperationalError as err:
            if 'no such table' in err.args[0]:
                raise TableNotFoundException(
                    table=self.table)
            raise

    def read(self, session, filters, mode):
        try:
            objects = self.__get_objects_with_filters(
                query=session.query(self._table),
                filters=filters,
                mode=mode)

            if not objects:
                raise ObjectNotFoundException(
                    filters=filters,
                    table=self._table)
        except FilterException:
            raise
        return objects

    def delete(self, session, filters, mode):
        try:
            object_from_db = self.read(
                session=session,
                filters=filters,
                mode=mode)[0]

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

from stuart.exceptions.database.database_exception import DatabaseException


class ObjectNotFoundException(DatabaseException):

    def __init__(self, table, filters):
        super(ObjectNotFoundException, self)
        self.status_code = 404
        self.table_name = table.table_name()
        self.filters = filters
        self.message = "Object '{}' not found with filters {} " \
                       "on database.".format(self.table_name, self.filters)

    @property
    def serialize(self):
        return {
            'status':       self.status_code,
            'table':        self.table_name,
            'filters':      self.filters,
            'message':      self.message
        }

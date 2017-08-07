from stuart.exceptions.database.database_exception import DatabaseException


class EmptyTableException(DatabaseException):

    def __init__(self, table):
        super(EmptyTableException, self)
        self.status_code = 204
        self.table_name = table.table_name()
        self.message = "No objects {} found on database.".format(self.table_name)

    @property
    def serialize(self):
        return {
            'status':       self.status_code,
            'table':        self.table_name,
            'message':      self.message
        }

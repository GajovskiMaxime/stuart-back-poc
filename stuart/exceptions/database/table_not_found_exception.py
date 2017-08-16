from stuart.exceptions.database.database_exception import DatabaseException


class TableNotFoundException(DatabaseException):

    def __init__(self, table):
        super(TableNotFoundException, self)
        self.status_code = 400
        self.table_name = table.table_name()
        self.message = "Table '{}' not found on database.".format(self.table_name)

    @property
    def serialize(self):
        return {
            'status':       self.status_code,
            'table':        self.table_name,
            'message':      self.message
        }

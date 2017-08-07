from stuart.exceptions.database.database_exception import DatabaseException


class LockedDatabaseException(DatabaseException):

    def __init__(self, action, table):
        super(LockedDatabaseException, self)
        self.status_code = 400
        self.action = action
        self.object_name = table.table_name()
        self.message = "Database is currently used by another program.\n" \
                       "Object '{}' can't be {}d.".format(self.object_name, self.action)

    @property
    def serialize(self):
        return {
            'status':       self.status_code,
            'action':       self.action,
            'object':       self.object_name,
            'message':      self.message
        }

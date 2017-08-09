from stuart.exceptions.database.database_exception import DatabaseException


class UniqueConstraintException(DatabaseException):

    def __init__(self, table, action, object_id):
        super(UniqueConstraintException, self)
        self.status_code = 400
        self.table_name = table.table_name()
        self.action = action
        self.object_id = object_id
        self.message = "Object '{}' can't be {}d.\n" \
                       "A similar entry already exist with id '{}'."\
            .format(self.table_name, self.action, self.object_id)

    @property
    def serialize(self):
        return {
            'status':       self.status_code,
            'table':        self.table_name,
            'object_id':    self.object_id,
            'action':       self.action,
            'message':      self.message
        }

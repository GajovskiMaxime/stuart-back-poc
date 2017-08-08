from stuart.exceptions.database.database_exception import DatabaseException


class UniqueConstraintException(DatabaseException):

    def __init__(self, table, action):
        super(UniqueConstraintException, self)
        self.status_code = 400
        self.table_name = table.table_name()
        self.action = action
        self.message = "Object '{}' can't be {}d.\n" \
                       "A similar entry already exist with same parameters."\
            .format(self.table_name, self.action, self.args)

    @property
    def serialize(self):
        return {
            'status':  self.status_code,
            'table':   self.table_name,
            'action':  self.action,
            'message': self.message
        }

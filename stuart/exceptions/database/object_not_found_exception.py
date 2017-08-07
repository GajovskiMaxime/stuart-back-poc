from stuart.exceptions.database.database_exception import DatabaseException


class ObjectNotFoundException(DatabaseException):

    def __init__(self, table, object_id):
        super(ObjectNotFoundException, self)
        self.status_code = 404
        self.table_name = table.table_name()
        self.object_id = object_id
        self.message = "Object {} with id {} not found " \
                       "on database.".format(self.table_name, self.object_id)

    @property
    def serialize(self):
        return {
            'status':       self.status_code,
            'table':        self.table_name,
            'id':           self.object_id,
            'message':      self.message
        }

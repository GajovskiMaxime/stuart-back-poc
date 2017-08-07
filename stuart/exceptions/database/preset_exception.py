from stuart.exceptions.database.database_exception import DatabaseException


class PresetException(DatabaseException):

    def __init__(self, table, object_id, action):
        super(PresetException, self)
        self.status_code = 400
        self.table_name = table.table_name()
        self.action = action
        self.object_id = object_id
        self.message = "Object {} with id {} is a preset, it can't be {}." \
                       .format(self.table_name, self.object_id, str(self.action + 'd'))

    @property
    def serialize(self):
        return {
            'status':   self.status_code,
            'object':   self.table_name,
            'id':       self.object_id,
            'action':   self.action,
            'message':  self.message
        }

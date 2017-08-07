from stuart.exceptions.database.database_exception import DatabaseException


class FilterException(DatabaseException):

    def __init__(self, filters):
        super(FilterException, self)
        self.status_code = 404
        self.filters = filters
        self.message = "Something wrong occurs with the filter {}." \
                       .format(self.filters)

    @property
    def serialize(self):
        return {
            'status':       self.status_code,
            'filters':      self.filters,
            'message':      self.message
        }

from stuart.exceptions.format.format_exception import FormatException


class IdIsNotAnIntegerException(FormatException):

    def __init__(self, table, attribute_value):
        super(IdIsNotAnIntegerException, self)
        self.status_code = 400
        self.attribute_value = attribute_value
        self.table = table.table_name()
        self.message = "On table {}, attribute 'id' with value {} " \
                       "must be an integer.".format(self.table, self.attribute_value)

    @property
    def serialize(self):
        return {
            'status':           self.status_code,
            'attribute_value':  self.attribute_value,
            'message':          self.message
        }

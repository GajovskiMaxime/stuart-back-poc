from stuart.exceptions.attribute.attribute_exception import AttributeException


class UnexpectedAttributeException(AttributeException):

    def __init__(self, unexpected_key, unexpected_value):
        super(UnexpectedAttributeException, self)
        self.status_code = 400
        self.unexpected_key = unexpected_key
        self.unexpected_value = unexpected_value
        self.message = "Unexpected key {} with value {}."\
            .format(self.unexpected_key, self.unexpected_value)

    @property
    def serialize(self):
        return {
            'status':           self.status_code,
            'unexpected_key':   self.unexpected_key,
            'unexpected_value': self.unexpected_value,
            'message':          self.message
        }

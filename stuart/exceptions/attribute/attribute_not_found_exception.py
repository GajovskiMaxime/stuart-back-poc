from stuart.exceptions.attribute.attribute_exception import AttributeException


class AttributeNotFoundException(AttributeException):

    def __init__(self, needed_attributes, table):
        super(AttributeNotFoundException, self)
        self.status_code = 400
        self.object = table.table_name()
        self.needed_attributes = str(needed_attributes).strip('[]')
        self.message = "Attributes : {} needed for object {}" \
            .format(self.needed_attributes, self.object)

    @property
    def serialize(self):
        return {
            'status':               self.status_code,
            'object':               self.object,
            'needed_attributes':    self.needed_attributes,
            'message':              self.message
        }

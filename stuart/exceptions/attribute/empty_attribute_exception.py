from stuart.exceptions.attribute.attribute_exception import AttributeException


class EmptyAttributeException(AttributeException):

    def __init__(self, table, attribute):
        super(EmptyAttributeException, self)
        self.status_code = 400
        self.attribute = attribute
        self.object_name = table.table_name()
        self.message = "Attribute '{}' for object '{}' is empty."\
            .format(self.attribute, self.object_name)

    @property
    def serialize(self):
        return {
            'status':       self.status_code,
            'attribute':    self.attribute,
            'object_name':  self.object_name,
            'message':      self.message
        }

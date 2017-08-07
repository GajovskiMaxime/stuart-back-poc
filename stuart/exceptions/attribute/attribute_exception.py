from stuart.exceptions.service_exception import ServiceException


class AttributeException(ServiceException):

    def __init__(self):
        super(AttributeException, self)

    @property
    def serialize(self):
        return {}

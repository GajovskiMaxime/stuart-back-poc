from stuart.exceptions.service_exception import ServiceException


class FormatException(ServiceException):

    def __init__(self):
        super(FormatException, self)

    @property
    def serialize(self):
        return {}

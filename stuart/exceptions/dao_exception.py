from stuart.exceptions.service_exception import ServiceException


class DAOException(ServiceException):

    def __init__(self):
        super(DAOException, self)

    @property
    def serialize(self):
        return {}

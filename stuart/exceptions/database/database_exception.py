from stuart.exceptions.dao_exception import DAOException


class DatabaseException(DAOException):

    def __init__(self):
        super(DatabaseException, self)

    @property
    def serialize(self):
        return {}

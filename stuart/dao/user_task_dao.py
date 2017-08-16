from stuart.dao.generic_dao import GenericDAO
from stuart.models.user_task import UserTask


class UserTaskDAO(GenericDAO):
    """
        User Task DAO class.
        -----------------
        :extends: GenericDAO
        :table: UserTask
    """
    def __init__(self):
        super(UserTaskDAO, self).__init__(
            table=UserTask)

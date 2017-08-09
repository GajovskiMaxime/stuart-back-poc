from stuart.dao.abstract_generic_dao import AbstractGenericDAO
from stuart.models.user_task import UserTask


class UserTaskDAO(AbstractGenericDAO):
    def __init__(self):
        super(UserTaskDAO, self).__init__(
            table=UserTask)

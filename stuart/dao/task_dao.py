from stuart.dao.abstract_generic_dao import AbstractGenericDAO
from stuart.models.task import Task


class TaskDAO(AbstractGenericDAO):
    def __init__(self):
        super(TaskDAO, self).__init__(
            table=Task)

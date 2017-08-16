from stuart.dao.generic_dao import GenericDAO
from stuart.models.task import Task


class TaskDAO(GenericDAO):
    """
        Task DAO class.
        -----------------
        :extends: GenericDAO
        :table: Task
    """
    def __init__(self):
        super(TaskDAO, self).__init__(
            table=Task)

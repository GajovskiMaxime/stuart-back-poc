from stuart.dao.generic_dao import GenericDAO
from stuart.models.task_params import TaskParams


class TaskParamsDAO(GenericDAO):
    """
        Task Params DAO class.
        -----------------
        :extends: GenericDAO
        :table: TaskParams
    """
    def __init__(self):
        super(TaskParamsDAO, self).__init__(
            table=TaskParams)

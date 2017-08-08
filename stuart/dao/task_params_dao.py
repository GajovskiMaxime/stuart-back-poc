from stuart.dao.abstract_generic_dao import AbstractGenericDAO
from stuart.models.task_params import TaskParams


class TaskParamsDAO(AbstractGenericDAO):
    def __init__(self):
        super(TaskParamsDAO, self).__init__(
            table=TaskParams)

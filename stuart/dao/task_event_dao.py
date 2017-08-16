from stuart.dao.generic_dao import GenericDAO
from stuart.models.task_event import TaskEvent


class TaskEventDAO(GenericDAO):
    """
        Task Event DAO class.
        -----------------
        :extends: GenericDAO
        :table: TaskEvent
    """
    def __init__(self):
        super(TaskEventDAO, self).__init__(
            table=TaskEvent)

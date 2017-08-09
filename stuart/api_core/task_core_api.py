from stuart.api_core.abstract_core_api import AbstractCoreAPI
from stuart.services.task_services import TaskService


class TaskCoreAPI(AbstractCoreAPI):
    def __init__(self):
        super(TaskCoreAPI, self).__init__(
            service=TaskService())

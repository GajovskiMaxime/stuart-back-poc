from stuart.api_core.generic_core_api import GenericCoreAPI
from stuart.services.task_services import TaskService


class TaskCoreAPI(GenericCoreAPI):
    """
          Task Core API class.
          -----------------
          :extends: GenericCoreAPI
          :service: TaskService
      """
    def __init__(self):
        super(TaskCoreAPI, self).\
            __init__(service=TaskService)

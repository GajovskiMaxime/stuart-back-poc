from stuart.api_core.generic_core_api import GenericCoreAPI
from stuart.services.task_event_services import TaskEventService


class TaskEventCoreAPI(GenericCoreAPI):
    """
          Task Event Core API class.
          -----------------
          :extends: GenericCoreAPI
          :service: TaskEventService
      """
    def __init__(self):
        super(TaskEventCoreAPI, self).\
            __init__(service=TaskEventService)

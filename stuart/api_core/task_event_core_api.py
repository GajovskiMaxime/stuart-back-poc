from stuart.api_core.abstract_core_api import AbstractCoreAPI
from stuart.services.task_event_services import TaskEventService


class TaskEventCoreAPI(AbstractCoreAPI):
    def __init__(self):
        super(TaskEventCoreAPI, self).__init__(
            service=TaskEventService())

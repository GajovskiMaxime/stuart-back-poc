from stuart.api_core.abstract_core_api import AbstractCoreAPI
from stuart.services.user_task_services import UserTaskService


class UserTaskCoreAPI(AbstractCoreAPI):
    def __init__(self):
        super(UserTaskCoreAPI, self).__init__(
            service=UserTaskService())

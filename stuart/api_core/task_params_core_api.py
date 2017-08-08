from stuart.api_core.abstract_core_api import AbstractCoreAPI
from stuart.services.task_params_services import TaskParamsService


class TaskParamsCoreAPI(AbstractCoreAPI):
    def __init__(self):
        super(TaskParamsCoreAPI, self).__init__(
            service=TaskParamsService())

from stuart.api_core.generic_core_api import GenericCoreAPI
from stuart.services.task_params_services import TaskParamsService


class TaskParamsCoreAPI(GenericCoreAPI):
    """
          Task Params Core API class.
          -----------------
          :extends: GenericCoreAPI
          :service: TaskParamsService
      """
    def __init__(self):
        super(TaskParamsCoreAPI, self).\
            __init__(service=TaskParamsService)

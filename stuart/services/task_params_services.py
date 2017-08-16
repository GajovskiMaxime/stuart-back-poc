from stuart.dao.task_params_dao import TaskParamsDAO
from stuart.services.generic_services import GenericService
from stuart.verifiers.task_params_verifier import TaskParamsVerifier


class TaskParamsService(GenericService):
    """
        Task Params Service class.
        -----------------
        :extends: GenericService
        :dao: TaskParamsDAO
        :verifier: TaskParamsVerifier
    """
    def __init__(self):
        super(TaskParamsService, self).__init__(
            dao=TaskParamsDAO,
            verifier=TaskParamsVerifier)


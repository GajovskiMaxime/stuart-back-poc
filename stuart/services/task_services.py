from stuart.dao.task_dao import TaskDAO
from stuart.services.generic_services import GenericService
from stuart.verifiers.task_verifier import TaskVerifier


class TaskService(GenericService):
    def __init__(self):
        super(TaskService, self).__init__(
            dao=TaskDAO(),
            verifier=TaskVerifier())


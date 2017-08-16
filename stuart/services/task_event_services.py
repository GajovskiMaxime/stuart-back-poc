from stuart.dao.task_event_dao import TaskEventDAO
from stuart.services.generic_services import GenericService
from stuart.verifiers.task_event_verifier import TaskEventVerifier


class TaskEventService(GenericService):
    """
        Task Event Service class.
        -----------------
        :extends: GenericService
        :dao: TaskEventDAO
        :verifier: TaskEventVerifier
    """
    def __init__(self):
        super(TaskEventService, self).__init__(
            dao=TaskEventDAO,
            verifier=TaskEventVerifier)

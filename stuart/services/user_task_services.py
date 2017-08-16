from stuart.dao.user_task_dao import UserTaskDAO
from stuart.services.generic_services import GenericService
from stuart.verifiers.user_task_verifier import UserTaskVerifier


class UserTaskService(GenericService):
    def __init__(self):
        super(UserTaskService, self).__init__(
            dao=UserTaskDAO,
            verifier=UserTaskVerifier)


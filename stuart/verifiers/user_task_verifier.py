from stuart.models.user_task import UserTask
from stuart.verifiers.model_verifier import ModelVerifier


class UserTaskVerifier(ModelVerifier):

    def __init__(self):
        super(UserTaskVerifier, self).__init__(
            table=UserTask)

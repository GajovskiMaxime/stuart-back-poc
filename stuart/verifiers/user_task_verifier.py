from stuart.models.user_task import UserTask
from stuart.verifiers.model_verifier import ModelVerifier


class UserTaskVerifier(ModelVerifier):
    """
        User Task Verifier class.
        -----------------
        :extends: ModelVerifier
        :table: UserTask
    """
    def __init__(self):
        super(UserTaskVerifier, self).\
            __init__(table=UserTask)

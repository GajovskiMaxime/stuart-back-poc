from stuart.models.task import Task
from stuart.verifiers.model_verifier import ModelVerifier


class TaskVerifier(ModelVerifier):
    """
        Task Verifier class.
        -----------------
        :extends: ModelVerifier
        :table: Task
    """
    def __init__(self):
        super(TaskVerifier, self).\
            __init__(table=Task)

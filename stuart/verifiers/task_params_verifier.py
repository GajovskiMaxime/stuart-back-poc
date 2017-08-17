from stuart.models.task_params import TaskParams
from stuart.verifiers.model_verifier import ModelVerifier


class TaskParamsVerifier(ModelVerifier):
    """
        Task Params Verifier class.
        -----------------
        :extends: ModelVerifier
        :table: TaskParams
    """
    def __init__(self):
        super(TaskParamsVerifier, self).\
            __init__(table=TaskParams)

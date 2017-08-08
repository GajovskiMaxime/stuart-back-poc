from stuart.models.task_params import TaskParams
from stuart.verifiers.model_verifier import ModelVerifier


class TaskParamsVerifier(ModelVerifier):

    def __init__(self):
        super(TaskParamsVerifier, self).__init__(
            table=TaskParams)

    def verify(self, **args):
        return super(TaskParamsVerifier, self).\
            verify(**args)

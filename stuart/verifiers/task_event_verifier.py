from stuart.models.task_event import TaskEvent
from stuart.verifiers.model_verifier import ModelVerifier


class TaskEventVerifier(ModelVerifier):

    def __init__(self):
        super(TaskEventVerifier, self).__init__(
            table=TaskEvent)

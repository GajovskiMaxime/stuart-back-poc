from stuart.models.log_event import LogEvent
from stuart.verifiers.model_verifier import ModelVerifier


class LogEventVerifier(ModelVerifier):
    def __init__(self):
        super(LogEventVerifier, self).__init__(
            table=LogEvent)

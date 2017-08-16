from stuart.dao.log_event_dao import LogEventDAO
from stuart.services.generic_services import GenericService
from stuart.verifiers.log_event_verifier import LogEventVerifier


class LogEventService(GenericService):
    """
        Log Event Service class.
        -----------------
        :extends: GenericService
        :dao: LogEventDAO
        :verifier: LogEventVerifier
    """
    def __init__(self):
        super(LogEventService, self).__init__(
            dao=LogEventDAO,
            verifier=LogEventVerifier)

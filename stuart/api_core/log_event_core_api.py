from stuart.api_core.abstract_core_api import AbstractCoreAPI
from stuart.services.log_event_services import LogEventService


class LogEventCoreAPI(AbstractCoreAPI):
    def __init__(self):
        super(LogEventCoreAPI, self).__init__(
            service=LogEventService())

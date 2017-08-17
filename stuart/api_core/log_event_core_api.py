from stuart.api_core.generic_core_api import GenericCoreAPI
from stuart.services.log_event_services import LogEventService


class LogEventCoreAPI(GenericCoreAPI):
    """
          Log Event Core API class.
          -----------------
          :extends: GenericCoreAPI
          :service: LogEventService
      """
    def __init__(self):
        super(LogEventCoreAPI, self).\
            __init__(service=LogEventService)

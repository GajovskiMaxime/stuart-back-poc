from stuart.dao.generic_dao import GenericDAO
from stuart.models.log_event import LogEvent


class LogEventDAO(GenericDAO):
    """
        Log Event DAO class.
        -----------------
        :extends: GenericDAO
        :table: LogEvent
    """
    def __init__(self):
        super(LogEventDAO, self).__init__(
            table=LogEvent)

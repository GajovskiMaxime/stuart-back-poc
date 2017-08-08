from stuart.api_core.abstract_core_api import AbstractCoreAPI
from stuart.services.action_services import ActionService


class ActionCoreAPI(AbstractCoreAPI):
    def __init__(self):
        super().__init__(
            service=ActionService())

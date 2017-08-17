from stuart.api_core.generic_core_api import GenericCoreAPI
from stuart.services.action_services import ActionService


class ActionCoreAPI(GenericCoreAPI):
    """
          Action Core API class.
          -----------------
          :extends: GenericCoreAPI
          :service: ActionService
      """
    def __init__(self):
        super(ActionCoreAPI, self).\
            __init__(service=ActionService)

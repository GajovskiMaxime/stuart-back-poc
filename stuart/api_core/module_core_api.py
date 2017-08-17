from stuart.api_core.generic_core_api import GenericCoreAPI
from stuart.services.module_services import ModuleService


class ModuleCoreAPI(GenericCoreAPI):
    """
          Module Core API class.
          -----------------
          :extends: GenericCoreAPI
          :service: ModuleService
      """
    def __init__(self):
        super(ModuleCoreAPI, self).\
            __init__(service=ModuleService)

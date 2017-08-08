from stuart.api_core.abstract_core_api import AbstractCoreAPI
from stuart.services.module_services import ModuleService


class ModuleCoreAPI(AbstractCoreAPI):

    def __init__(self):
        super().__init__(
            service=ModuleService())

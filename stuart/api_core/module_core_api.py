from stuart.api_core.abstract_core_api import AbstractCoreAPI
from stuart.services.module_services import ModuleService


class ModuleCoreAPI(AbstractCoreAPI):

    def __init__(self):
        super().__init__(
            service=ModuleService())

    def read_all(self, filters):
        return super(ModuleCoreAPI, self). \
            read_all(
                filters=filters)

    def create(self, filters):
        return super(ModuleCoreAPI, self).\
            create(
                request=filters)

    def delete(self, filters):
        return super(ModuleCoreAPI, self).\
            delete(filters=filters)

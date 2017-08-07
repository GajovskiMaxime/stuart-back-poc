from stuart.dao.module_dao import ModuleDAO
from stuart.services.abstract_generic_services import AbstractGenericService
from stuart.verifiers.module_verifier import ModuleVerifier


class ModuleService(AbstractGenericService):

    def __init__(self):
        super(ModuleService, self).__init__(
            dao=ModuleDAO(),
            verifier=ModuleVerifier())

    def create_with_dict(self, **args):
        return super(ModuleService, self).\
            create_with_dict(**args)

    def read_all(self, filters):
        return super(ModuleService, self).\
            read_all(filters=filters)

    def delete(self, filters):
        return super(ModuleService, self).\
            delete(filters=filters)

from stuart.dao.module_dao import ModuleDAO
from stuart.services.generic_services import GenericService
from stuart.verifiers.module_verifier import ModuleVerifier


class ModuleService(GenericService):

    def __init__(self):
        super(ModuleService, self).__init__(
            dao=ModuleDAO(),
            verifier=ModuleVerifier())

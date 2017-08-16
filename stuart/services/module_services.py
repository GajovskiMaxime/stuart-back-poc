from stuart.dao.module_dao import ModuleDAO
from stuart.services.generic_services import GenericService
from stuart.verifiers.module_verifier import ModuleVerifier


class ModuleService(GenericService):
    """
        Module Service class.
        -----------------
        :extends: GenericService
        :dao: ModuleDAO
        :verifier: ModuleVerifier
    """
    def __init__(self):
        super(ModuleService, self).__init__(
            dao=ModuleDAO,
            verifier=ModuleVerifier)

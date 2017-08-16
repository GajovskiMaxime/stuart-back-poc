from stuart.dao.generic_params_patterns_dao import GenericParamsPatternsDAO
from stuart.services.generic_services import GenericService
from stuart.verifiers.generic_params_patterns_verifier import GenericParamsPatternsVerifier


class GenericParamsPatternsService(GenericService):
    """
        Generic Params Patterns Service class.
        -----------------
        :extends: GenericService
        :dao: GenericParamsPatternsDAO
        :verifier: GenericParamsPatternsVerifier
    """
    def __init__(self):
        super(GenericParamsPatternsService, self).__init__(
            dao=GenericParamsPatternsDAO,
            verifier=GenericParamsPatternsVerifier)

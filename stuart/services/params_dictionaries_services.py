from stuart.dao.params_dictionaries_dao import ParamsDictionariesDAO
from stuart.services.generic_services import GenericService
from stuart.verifiers.params_dictionaries_verifier import ParamsDictionariesVerifier


class ParamsDictionariesService(GenericService):
    """
        Params Dictionaries Service class.
        -----------------
        :extends: GenericService
        :dao: ParamsDictionariesDAO
        :verifier: ParamsDictionariesVerifier
    """
    def __init__(self):
        super(ParamsDictionariesService, self).__init__(
            dao=ParamsDictionariesDAO,
            verifier=ParamsDictionariesVerifier)

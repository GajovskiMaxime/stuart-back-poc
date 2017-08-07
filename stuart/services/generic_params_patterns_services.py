from stuart.dao.generic_params_patterns_dao import GenericParamsPatternsDAO
from stuart.services.abstract_generic_services import AbstractGenericService
from stuart.verifiers.generic_params_patterns_verifier import GenericParamsPatternsVerifier


class GenericParamsPatternService(AbstractGenericService):

    def __init__(self):
        super(GenericParamsPatternService, self).__init__(
            dao=GenericParamsPatternsDAO(),
            verifier=GenericParamsPatternsVerifier())

    def create_with_dict(self, **args):
        return super(GenericParamsPatternService, self).\
            create_with_dict(**args)

    def read_all(self, filters):
        return super(GenericParamsPatternService, self).\
            read_all(filters=filters)

    def delete(self, filters):
        return super(GenericParamsPatternService, self).\
            delete(filters=filters)

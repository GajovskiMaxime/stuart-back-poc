from stuart.dao.params_dictionaries_dao import ParamsDictionariesDAO
from stuart.services.abstract_generic_services import AbstractGenericService
from stuart.verifiers.params_dictionaries_verifier import ParamsDictionariesVerifier


class ParamsDictionariesService(AbstractGenericService):

    def __init__(self):
        super(ParamsDictionariesService, self).__init__(
            dao=ParamsDictionariesDAO(),
            verifier=ParamsDictionariesVerifier())

    def create_with_dict(self, **args):
        return super(ParamsDictionariesService, self).\
            create_with_dict(**args)

    def read_all(self, filters):
        return super(ParamsDictionariesService, self).\
            read_all(filters=filters)

    def delete(self, filters):
        return super(ParamsDictionariesService, self).\
            delete(filters=filters)

from stuart.api_core.abstract_core_api import AbstractCoreAPI
from stuart.services.params_dictionaries_services import ParamsDictionariesService


class ParamsDictionariesCoreAPI(AbstractCoreAPI):

    def __init__(self):
        super(ParamsDictionariesCoreAPI, self).__init__(
            service=ParamsDictionariesService())

    def read_all(self, filters):
        return super(ParamsDictionariesCoreAPI, self). \
            read_all(
                filters=filters)

    def create(self, filters):
        return super(ParamsDictionariesCoreAPI, self).\
            create(
                request=filters)

    def delete(self, filters):
        return super(ParamsDictionariesCoreAPI, self).\
            delete(filters=filters)

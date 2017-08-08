from stuart.api_core.abstract_core_api import AbstractCoreAPI
from stuart.services.params_dictionaries_services import ParamsDictionariesService


class ParamsDictionariesCoreAPI(AbstractCoreAPI):
    def __init__(self):
        super(ParamsDictionariesCoreAPI, self).__init__(
            service=ParamsDictionariesService())

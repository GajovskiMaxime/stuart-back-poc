from stuart.api_core.generic_core_api import GenericCoreAPI
from stuart.services.params_dictionaries_services import ParamsDictionariesService


class ParamsDictionariesCoreAPI(GenericCoreAPI):
    """
          Params Dictionaries Core API class.
          -----------------
          :extends: GenericCoreAPI
          :service: ParamsDictionariesService
      """
    def __init__(self):
        super(ParamsDictionariesCoreAPI, self).\
            __init__(service=ParamsDictionariesService)

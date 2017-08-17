from stuart.api_core.generic_core_api import GenericCoreAPI
from stuart.services.generic_params_patterns_services import GenericParamsPatternsService


class GenericParamsPatternsCoreAPI(GenericCoreAPI):
    """
          Generic Params Patterns Core API class.
          -----------------
          :extends: GenericCoreAPI
          :service: GenericParamsPatternsService
      """
    def __init__(self):
        super(GenericParamsPatternsCoreAPI, self).\
            __init__(service=GenericParamsPatternsService)

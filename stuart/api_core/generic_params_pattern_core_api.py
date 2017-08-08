from stuart.api_core.abstract_core_api import AbstractCoreAPI
from stuart.services.generic_params_patterns_services import GenericParamsPatternsService


class GenericParamsPatternsCoreAPI(AbstractCoreAPI):

    def __init__(self):
        super(GenericParamsPatternsCoreAPI, self).__init__(
            service=GenericParamsPatternsService())

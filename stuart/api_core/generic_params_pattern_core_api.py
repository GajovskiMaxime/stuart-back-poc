from stuart.api_core.abstract_core_api import AbstractCoreAPI
from stuart.services.generic_params_patterns_services import GenericParamsPatternService


class GenericParamsPatternsCoreAPI(AbstractCoreAPI):

    def __init__(self):
        super(GenericParamsPatternsCoreAPI, self).__init__(
            service=GenericParamsPatternService())

    def read_all(self, filters):
        return super(GenericParamsPatternsCoreAPI, self). \
            read_all(
                filters=filters)

    def create(self, filters):
        return super(GenericParamsPatternsCoreAPI, self).\
            create(
                request=filters)

    def delete(self, filters):
        return super(GenericParamsPatternsCoreAPI, self).\
            delete(filters=filters)

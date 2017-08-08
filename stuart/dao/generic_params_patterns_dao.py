from stuart.dao.abstract_generic_dao import AbstractGenericDAO
from stuart.models.generic_params_patterns import GenericParamsPatterns


class GenericParamsPatternsDAO(AbstractGenericDAO):
    def __init__(self):
        super(GenericParamsPatternsDAO, self).__init__(
            table=GenericParamsPatterns)

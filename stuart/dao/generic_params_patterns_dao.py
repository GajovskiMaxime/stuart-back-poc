from stuart.dao.generic_dao import GenericDAO
from stuart.models.generic_params_patterns import GenericParamsPatterns


class GenericParamsPatternsDAO(GenericDAO):
    """
        Generic Params Patterns DAO class.
        -----------------
        :extends: GenericDAO
        :table: GenericParamsPatterns
    """
    def __init__(self):
        super(GenericParamsPatternsDAO, self).__init__(
            table=GenericParamsPatterns)

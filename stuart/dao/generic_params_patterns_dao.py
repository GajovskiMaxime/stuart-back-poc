from stuart.dao.abstract_generic_dao import AbstractGenericDAO
from stuart.models.generic_params_patterns import GenericParamsPatterns


class GenericParamsPatternsDAO(AbstractGenericDAO):

    def __init__(self):
        super(GenericParamsPatternsDAO, self).__init__(table=GenericParamsPatterns)

    def create(self, session, model):
        return super(GenericParamsPatternsDAO, self).create(
            session=session,
            model=model)

    def read_all(self, session, filters):
        return super(GenericParamsPatternsDAO, self).read_all(
            session=session,
            filters=filters)

    def delete(self, session, filters):
        return super(GenericParamsPatternsDAO, self).delete(
            session=session,
            filters=filters)

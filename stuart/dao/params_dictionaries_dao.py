from stuart.dao.abstract_generic_dao import AbstractGenericDAO
from stuart.models.params_dictionary import ParamsDictionaries


class ParamsDictionariesDAO(AbstractGenericDAO):

    def __init__(self):
        super(ParamsDictionariesDAO, self).__init__(
            table=ParamsDictionaries)

    def create(self, session, model):
        return super(ParamsDictionariesDAO, self).create(
            session=session,
            model=model)

    def read_all(self, session, filters):
        return super(ParamsDictionariesDAO, self).read_all(
            session=session,
            filters=filters)

    def delete(self, session, filters):
        return super(ParamsDictionariesDAO, self).delete(
            session=session,
            filters=filters)

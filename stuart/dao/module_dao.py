from stuart.dao.abstract_generic_dao import AbstractGenericDAO
from stuart.models.module import Module


class ModuleDAO(AbstractGenericDAO):

    def __init__(self):
        super(ModuleDAO, self).__init__(table=Module)

    def create(self, session, model):
        return super(ModuleDAO, self).create(
            session=session,
            model=model)

    def read_all(self, session, filters):
        return super(ModuleDAO, self).read_all(
            session=session,
            filters=filters)

    def delete(self, session, filters):
        return super(ModuleDAO, self).delete(
            session=session,
            filters=filters)

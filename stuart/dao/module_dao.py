from stuart.dao.abstract_generic_dao import AbstractGenericDAO
from stuart.models.module import Module


class ModuleDAO(AbstractGenericDAO):

    def __init__(self):
        super(ModuleDAO, self).__init__(table=Module)

    def create(self, session, model):
        return super(ModuleDAO, self).create(
            session=session,
            model=model)

    def read_by_id(self, session, object_id):
        return super(ModuleDAO, self).read_by_id(
            session=session,
            object_id=object_id)

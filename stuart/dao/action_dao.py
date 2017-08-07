from stuart.dao.abstract_generic_dao import AbstractGenericDAO
from stuart.models.action import Action


class ActionDAO(AbstractGenericDAO):

    def __init__(self):
        super(ActionDAO, self).__init__(table=Action)

    def create(self, session, model):
        return super(ActionDAO, self).create(
            session=session,
            model=model)

    def read_by_id(self, session, object_id):
        return super(ActionDAO, self).read_by_id(
            session=session,
            object_id=object_id)

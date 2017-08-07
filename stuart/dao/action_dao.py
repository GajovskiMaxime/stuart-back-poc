from stuart.dao.abstract_generic_dao import AbstractGenericDAO
from stuart.models.action import Action


class ActionDAO(AbstractGenericDAO):

    def __init__(self):
        super(ActionDAO, self).__init__(table=Action)

    def create(self, session, model):
        return super(ActionDAO, self).create(
            session=session,
            model=model)

    def read_all(self, session, filters):
        return super(ActionDAO, self).read_all(
            session=session,
            filters=filters)

    def delete(self, session, filters):
        return super(ActionDAO, self).delete(
            session=session,
            filters=filters)

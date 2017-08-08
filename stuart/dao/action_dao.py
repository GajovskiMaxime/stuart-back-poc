from stuart.dao.abstract_generic_dao import AbstractGenericDAO
from stuart.models.action import Action


class ActionDAO(AbstractGenericDAO):

    def __init__(self):
        super(ActionDAO, self).__init__(
            table=Action)

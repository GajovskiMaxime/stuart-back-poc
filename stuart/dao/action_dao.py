from stuart.dao.generic_dao import GenericDAO
from stuart.models.action import Action


class ActionDAO(GenericDAO):
    """
        Action DAO class.
        -----------------
        :extends: GenericDAO
        :table: Action
    """
    def __init__(self):
        super(ActionDAO, self).__init__(
            table=Action)

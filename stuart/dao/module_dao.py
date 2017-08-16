from stuart.dao.generic_dao import GenericDAO
from stuart.models.module import Module


class ModuleDAO(GenericDAO):
    """
        Module DAO class.
        -----------------
        :extends: GenericDAO
        :table: Module
    """
    def __init__(self):
        super(ModuleDAO, self).__init__(
            table=Module)

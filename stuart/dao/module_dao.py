from stuart.dao.abstract_generic_dao import AbstractGenericDAO
from stuart.models.module import Module


class ModuleDAO(AbstractGenericDAO):
    def __init__(self):
        super(ModuleDAO, self).__init__(
            table=Module)

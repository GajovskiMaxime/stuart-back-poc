from stuart.dao.abstract_generic_dao import AbstractGenericDAO
from stuart.models.params_dictionary import ParamsDictionaries


class ParamsDictionariesDAO(AbstractGenericDAO):
    def __init__(self):
        super(ParamsDictionariesDAO, self).__init__(
            table=ParamsDictionaries)

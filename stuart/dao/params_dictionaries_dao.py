from stuart.dao.generic_dao import GenericDAO
from stuart.models.params_dictionary import ParamsDictionaries


class ParamsDictionariesDAO(GenericDAO):
    """
        Params Dictionaries DAO class.
        -----------------
        :extends: GenericDAO
        :table: ParamsDictionaries
    """
    def __init__(self):
        super(ParamsDictionariesDAO, self).__init__(
            table=ParamsDictionaries)

from stuart.models.params_dictionary import ParamsDictionaries
from stuart.verifiers.model_verifier import ModelVerifier


class ParamsDictionariesVerifier(ModelVerifier):
    """
        Params Dictionaries Verifier class.
        -----------------
        :extends: ModelVerifier
        :table: ParamsDictionaries
    """
    def __init__(self):
        super(ParamsDictionariesVerifier, self).\
            __init__(table=ParamsDictionaries)

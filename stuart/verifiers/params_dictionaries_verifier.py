from stuart.models.params_dictionary import ParamsDictionaries
from stuart.verifiers.model_verifier import ModelVerifier


class ParamsDictionariesVerifier(ModelVerifier):

    def __init__(self):
        super(ParamsDictionariesVerifier, self).__init__(
            table=ParamsDictionaries)

    def verify_args(self, **args):
        return super(ParamsDictionariesVerifier, self).\
            verify_args(**args)

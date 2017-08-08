from stuart.models.generic_params_patterns import GenericParamsPatterns
from stuart.verifiers.model_verifier import ModelVerifier


class GenericParamsPatternsVerifier(ModelVerifier):

    def __init__(self):
        super(GenericParamsPatternsVerifier, self).__init__(
            table=GenericParamsPatterns)

    def verify(self, **args):
        return super(GenericParamsPatternsVerifier, self).\
            verify(**args)

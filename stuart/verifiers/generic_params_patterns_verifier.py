from stuart.models.generic_params_patterns import GenericParamsPatterns
from stuart.verifiers.model_verifier import ModelVerifier


class GenericParamsPatternsVerifier(ModelVerifier):

    def __init__(self):
        super(GenericParamsPatternsVerifier, self).__init__(
            table=GenericParamsPatterns)

    def verify_args(self, **args):
        return super(GenericParamsPatternsVerifier, self).\
            verify_args(**args)

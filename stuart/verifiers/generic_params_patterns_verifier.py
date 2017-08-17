from stuart.models.generic_params_patterns import GenericParamsPatterns
from stuart.verifiers.model_verifier import ModelVerifier


class GenericParamsPatternsVerifier(ModelVerifier):
    """
        Generic Params Patterns Verifier class.
        -----------------
        :extends: ModelVerifier
        :table: GenericParamsPatterns
    """
    def __init__(self):
        super(GenericParamsPatternsVerifier, self).\
            __init__(table=GenericParamsPatterns)

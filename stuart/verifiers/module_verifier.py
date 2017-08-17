from stuart.models.module import Module
from stuart.verifiers.model_verifier import ModelVerifier


class ModuleVerifier(ModelVerifier):
    """
        Module Verifier class.
        -----------------
        :extends: ModelVerifier
        :table: Module
    """
    def __init__(self):
        super(ModuleVerifier, self).__init__(
            table=Module)

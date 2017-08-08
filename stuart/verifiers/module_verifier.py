from stuart.models.module import Module
from stuart.verifiers.model_verifier import ModelVerifier


class ModuleVerifier(ModelVerifier):

    def __init__(self):
        super(ModuleVerifier, self).__init__(
            table=Module)

    def verify(self, **args):
        return super(ModuleVerifier, self).verify(**args)

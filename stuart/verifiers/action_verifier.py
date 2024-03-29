from stuart.models.action import Action
from stuart.verifiers.model_verifier import ModelVerifier


class ActionVerifier(ModelVerifier):
    """
        Action Verifier class.
        -----------------
        :extends: ModelVerifier
        :table: Action
    """
    def __init__(self):
        super(ActionVerifier, self).\
            __init__(table=Action)

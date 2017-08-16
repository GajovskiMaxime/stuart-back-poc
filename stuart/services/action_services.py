from stuart.dao.action_dao import ActionDAO
from stuart.services.generic_services import GenericService
from stuart.verifiers.action_verifier import ActionVerifier


class ActionService(GenericService):
    """
        Action Service class.
        -----------------
        :extends: GenericService
        :dao: ActionDAO
        :verifier: ActionVerifier
    """
    def __init__(self):
        super(ActionService, self).__init__(
            dao=ActionDAO,
            verifier=ActionVerifier)

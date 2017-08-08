from stuart.dao.action_dao import ActionDAO
from stuart.services.generic_services import GenericService
from stuart.verifiers.action_verifier import ActionVerifier


class ActionService(GenericService):
    def __init__(self):
        super(ActionService, self).__init__(
            dao=ActionDAO(),
            verifier=ActionVerifier())

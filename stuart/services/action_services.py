from stuart.dao.action_dao import ActionDAO
from stuart.services.abstract_generic_services import AbstractGenericService
from stuart.verifiers.action_verifier import ActionVerifier


class ActionService(AbstractGenericService):

    def __init__(self):
        super(ActionService, self).__init__(
            dao=ActionDAO(),
            verifier=ActionVerifier())

    def create_with_dict(self, **args):
        return super(ActionService, self). \
            create_with_dict(**args)

    def read_all(self, filters):
        return super(ActionService, self).\
            read_all(filters=filters)

    def delete(self, filters):
        return super(ActionService, self).\
            delete(filters=filters)

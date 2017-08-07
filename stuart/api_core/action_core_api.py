from stuart.api_core.abstract_core_api import AbstractCoreAPI
from stuart.services.action_services import ActionService


class ActionCoreAPI(AbstractCoreAPI):

    def __init__(self):
        super().__init__(
            service=ActionService())

    def read_all(self, filters):
        return super(ActionCoreAPI, self). \
            read_all(
                filters=filters)

    def create(self, filters):
        return super(ActionCoreAPI, self).\
            create(request=filters)

    def delete(self, filters):
        return super(ActionCoreAPI, self).\
            delete(filters=filters)

from stuart.exceptions.service_exception import ServiceException


class JSONException(ServiceException):

    def __init__(self):
        super(JSONException, self)

    @property
    def serialize(self):
        return {}

from stuart.exceptions.json.json_exception import JSONException


class MissingObjectOnJSONRequest(JSONException):

    def __init__(self, requested_object_name):
        super(MissingObjectOnJSONRequest, self)
        self.status_code = 400
        self.request_object_name = requested_object_name
        self.message = "Missing object '{}' on json request."\
            .format(self.request_object_name)

    @property
    def serialize(self):
        return {
            'status':           self.status_code,
            'request_object':   self.request_object_name,
            'message':          self.message
        }

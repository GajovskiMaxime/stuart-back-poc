from stuart.exceptions.json.json_exception import JSONException


class MalformedJSONObjectException(JSONException):

    def __init__(self, key, value):
        super(MalformedJSONObjectException, self)
        self.status_code = 400
        self.key = key
        self.value = value
        self.message = "Object '{}' with value '{}' isn't a json object."\
            .format(self.key, self.value)

    @property
    def serialize(self):
        return {
            'status':   self.status_code,
            'key':      self.key,
            'value':    self.value,
            'message':  self.message
        }

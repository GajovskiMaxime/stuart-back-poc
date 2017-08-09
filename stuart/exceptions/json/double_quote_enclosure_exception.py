from stuart.exceptions.json.json_exception import JSONException


class DoubleQuoteEnclosureException(JSONException):

    def __init__(self, value):
        super(DoubleQuoteEnclosureException, self)
        self.status_code = 400
        self.value = value
        self.message = "Both keys and values into '{}'" \
                       " needed to be enclosed with double quotes."\
            .format(self.value)

    @property
    def serialize(self):
        return {
            'status':   self.status_code,
            'value':    self.value,
            'message':  self.message
        }

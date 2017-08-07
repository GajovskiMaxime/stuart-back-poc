
from stuart.exceptions.json.missing_object_on_json_request import MissingObjectOnJSONRequest
from stuart.utils.api_utils import json_response


def list_to_json(lst):
    return [item.serialize for item in lst]


def get_object_from_request(request, requested_object_name):

    post_data = request.get_json()

    if not post_data \
            or requested_object_name not in post_data \
            or type(post_data[requested_object_name]) is not dict:
        raise MissingObjectOnJSONRequest(
            requested_object_name=requested_object_name)

    return post_data[requested_object_name]


def get_success_response(verb, table, object_id):
    table_name = table.table_name()
    message = "{} with id {} {}d successfully.".format(table_name.title(), object_id, verb)

    return json_response(
        status=200,
        object=table_name,
        id=object_id,
        message=message)


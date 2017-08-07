
from stuart.exceptions.json.missing_object_on_json_request import MissingObjectOnJSONRequest
from stuart.utils.api_utils import json_response


def list_to_json(lst):
    return [item.serialize for item in lst]


def list_to_json_lazy(lst):
    return [item.serialize_lazy for item in lst]


def list_to_json_with_lazy_attr(response, table_name, is_lazy):
    if is_lazy:
        return {str(table_name + '_list'): list_to_json_lazy(response)}
    return {str(table_name + '_list'): list_to_json(response)}


def object_to_json_with_lazy_attr(response, table_name, is_lazy):
    if is_lazy:
        return {table_name: response.serialize_lazy}
    return {table_name: response.serialize}


def get_object_from_request(request, requested_object_name):

    post_data = request.get_json()

    if not post_data \
            or requested_object_name not in post_data \
            or type(post_data[requested_object_name]) is not dict:
        raise MissingObjectOnJSONRequest(
            requested_object_name=requested_object_name)

    return post_data[requested_object_name]


def get_insensitive_filters_list(filters):
    insensitive_filters_list = {}
    for k, v in filters.items():
        if type(v) is str:
            insensitive_filters_list[k.lower()] = v.lower()
        else:
            insensitive_filters_list[k.lower()] = v
    return insensitive_filters_list


def split_into_lazy_arg_and_filters_list(filters):
    is_lazy = False
    if 'lazy' in filters:
        filters.pop('lazy', None)
        is_lazy = True
    return is_lazy, filters


def get_success_response(verb, table, object_id):
    table_name = table.table_name()
    message = "{} with id {} {}d successfully.".format(table_name.title(), object_id, verb)

    return json_response(
        status=200,
        object=table_name,
        id=object_id,
        message=message)


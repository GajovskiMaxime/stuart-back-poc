from flask import jsonify

from stuart.exceptions.service_exception import ServiceException
from stuart.utils.api_utils import json_response
from stuart.utils.json_utils import get_object_from_request, get_success_response, \
    list_to_json_with_lazy_attr, get_insensitive_filters_list, split_into_lazy_arg_and_filters_list, \
    object_to_json_with_lazy_attr


class GenericCoreAPI(object):

    def __init__(self, service):
        self._service = service()

    def read(self, filters):
        insensitive_filter_list = get_insensitive_filters_list(
            filters=filters)
        is_lazy, insensitive_filter_list = split_into_lazy_arg_and_filters_list(
            filters=insensitive_filter_list)
        try:
            response = self._service.read(
                filters=insensitive_filter_list,
                mode='contains')

            fct_response, response = (object_to_json_with_lazy_attr, response[0]) \
                if len(response) == 1 \
                else (list_to_json_with_lazy_attr, response)

        except ServiceException as e:
            return json_response(**e.serialize)
        return jsonify(fct_response(
            table_name=self._service.dao.table.table_name(),
            is_lazy=is_lazy,
            response=response
        ))

    def create(self, request):
        try:
            obj_from_request = get_object_from_request(
                request=request,
                requested_object_name=self._service.dao.table.table_name())

            created_obj = self._service.create(
                args=obj_from_request,
                autocommit=False)
        except ServiceException as err:
            return json_response(**err.serialize)

        return get_success_response(
            verb='create',
            table=self._service.dao.table,
            object_id=created_obj.id)

    def delete(self, filters):
        try:
            self._service.delete(
                filters=filters,
                mode='exact')
        except ServiceException as err:
            return json_response(**err.serialize)

        return get_success_response(
            verb='delete',
            table=self._service.dao.table,
            object_id=filters['id'])

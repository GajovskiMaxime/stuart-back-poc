from flask import jsonify, current_app

from stuart.exceptions.service_exception import ServiceException
from stuart.models.module import Module
from stuart.utils.api_utils import json_response
from stuart.utils.json_utils import get_object_from_request, get_success_response


class AbstractAPI(object):

    def __init__(self, service):
        self._service = service

    def read_by_id(self, object_id):
        try:
            response = self._service.read_by_id(
                object_id=object_id)
        except ServiceException as e:
            return json_response(**e.serialize)
        return jsonify(response.serialize)

    def create(self, request):
        try:
            obj_from_request = get_object_from_request(
                request=request,
                requested_object_name=self._service.dao.table.table_name())

            created_obj = self._service.create_with_dict(
                args=obj_from_request)
        except ServiceException as err:
            return json_response(**err.serialize)
        return get_success_response(
            verb='create',
            table=self._service.dao.table,
            object_id=created_obj.id)

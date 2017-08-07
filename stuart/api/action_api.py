from flask import Blueprint, request

from stuart.api.abstract_api import AbstractAPI
from stuart.services.action_services import ActionService


class ActionAPI(object):

    action_blueprint = Blueprint(
        'actions',
        __name__,
        url_prefix="/actions")

    @staticmethod
    @action_blueprint.route('/<string:module_id>', methods=['GET'])
    def read_by_id(module_id):
        return AbstractAPI(ActionService()).read_by_id(module_id)

    @staticmethod
    @action_blueprint.route('/', methods=['PUT'])
    def create():
        return AbstractAPI(ActionService()).create(request)

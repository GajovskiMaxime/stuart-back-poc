from flask import Blueprint, request

from stuart.api.abstract_api import AbstractAPI
from stuart.services.module_services import ModuleService


class ModuleAPI(object):

    module_blueprint = Blueprint(
        'modules',
        __name__,
        url_prefix="/modules")

    @staticmethod
    @module_blueprint.route('/<string:module_id>', methods=['GET'])
    def read_by_id(module_id):
        return AbstractAPI(ModuleService()).read_by_id(module_id)

    @staticmethod
    @module_blueprint.route('/', methods=['PUT'])
    def create():
        return AbstractAPI(ModuleService()).create(request)

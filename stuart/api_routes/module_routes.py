from flask import Blueprint, request

from stuart.api_core.module_core_api import ModuleCoreAPI


class ModuleRoutes(object):

    module_blueprint = Blueprint(
        'modules',
        __name__,
        url_prefix="/modules")

    @staticmethod
    @module_blueprint.route('/<string:module_id>/', methods=['GET'])
    def read_by_id(module_id):
        dictionary = request.args.to_dict()
        dictionary['id'] = module_id
        return ModuleCoreAPI().read(
            filters=dictionary)

    @staticmethod
    @module_blueprint.route('/', methods=['GET'])
    def read_all():
        dictionary = request.args.to_dict()
        return ModuleCoreAPI().read(
            filters=dictionary)

    @staticmethod
    @module_blueprint.route('/', methods=['PUT'])
    def create():
        return ModuleCoreAPI().create(request)

    @staticmethod
    @module_blueprint.route('/<string:module_id>/', methods=['DELETE'])
    def delete(module_id):
        dictionary = request.args.to_dict()
        dictionary['id'] = module_id
        return ModuleCoreAPI().delete(
            filters=dictionary)

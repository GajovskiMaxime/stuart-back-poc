from flask import Blueprint, request, current_app

from stuart.api_core.action_core_api import ActionCoreAPI


class ActionRoutes(object):

    action_blueprint = Blueprint(
        'actions',
        __name__,
        url_prefix="/modules/<string:module_id>/actions")

    # TODO: No control on module_id
    # TODO: No joker '*' for all actions
    @staticmethod
    @action_blueprint.route('/<string:action_id>/', methods=['GET'])
    def read_by_id(module_id, action_id):
        dictionary = request.args.to_dict()
        dictionary['id'] = action_id
        dictionary['module_id'] = module_id
        return ActionCoreAPI().read_all(
            filters=dictionary)

    # TODO: No control on module_id
    @staticmethod
    @action_blueprint.route('/', methods=['GET'])
    def read_all(module_id):
        dictionary = request.args.to_dict()
        dictionary['module_id'] = module_id
        return ActionCoreAPI().read_all(
            filters=dictionary)

    @staticmethod
    @action_blueprint.route('/', methods=['PUT'])
    def create(module_id):
        return ActionCoreAPI().create(filters=request)

    @staticmethod
    @action_blueprint.route('/<string:action_id>/', methods=['DELETE'])
    def delete(module_id, action_id):
        dictionary = request.args.to_dict()
        dictionary['id'] = action_id
        dictionary['module_id'] = module_id
        return ActionCoreAPI().delete(
            filters=dictionary)

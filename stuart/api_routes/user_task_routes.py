from flask import Blueprint, request

from stuart.api_core.user_task_core_api import UserTaskCoreAPI


class UserTaskRoutes(object):

    user_task_blueprint = Blueprint(
        'userTasks',
        __name__,
        url_prefix="/userTasks")

    @staticmethod
    @user_task_blueprint.route('/<string:user_task_id>/', methods=['GET'])
    def read_by_id(user_task_id):
        dictionary = request.args.to_dict()
        dictionary['id'] = user_task_id
        return UserTaskCoreAPI().read(
            filters=dictionary)

    @staticmethod
    @user_task_blueprint.route('/', methods=['GET'])
    def read_all():
        dictionary = request.args.to_dict()
        return UserTaskCoreAPI().read(
            filters=dictionary)

    @staticmethod
    @user_task_blueprint.route('/', methods=['PUT'])
    def create():
        return UserTaskCoreAPI().create(request)

    @staticmethod
    @user_task_blueprint.route('/<string:user_task_id>/', methods=['DELETE'])
    def delete(user_task_id):
        dictionary = request.args.to_dict()
        dictionary['id'] = user_task_id
        return UserTaskCoreAPI().delete(
            filters=dictionary)

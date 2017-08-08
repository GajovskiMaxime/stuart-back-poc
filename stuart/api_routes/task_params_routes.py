from flask import Blueprint, request
from stuart.api_core.task_params_core_api import TaskParamsCoreAPI


class TaskParamsRoutes(object):

    task_params_blueprint = Blueprint(
        'task_params',
        __name__,
        url_prefix="/task_params")

    @staticmethod
    @task_params_blueprint.route('/<string:task_param_id>/', methods=['GET'])
    def read_by_id(task_param_id):
        dictionary = request.args.to_dict()
        dictionary['id'] = task_param_id
        return TaskParamsCoreAPI().read(
            filters=dictionary)

    @staticmethod
    @task_params_blueprint.route('/', methods=['GET'])
    def read_all():
        dictionary = request.args.to_dict()
        return TaskParamsCoreAPI().read(
            filters=dictionary)

    @staticmethod
    @task_params_blueprint.route('/', methods=['PUT'])
    def create():
        return TaskParamsCoreAPI().create(request)

    @staticmethod
    @task_params_blueprint.route('/<string:module_id>/', methods=['DELETE'])
    def delete(module_id):
        dictionary = request.args.to_dict()
        dictionary['id'] = module_id
        return TaskParamsCoreAPI().delete(
            filters=dictionary)

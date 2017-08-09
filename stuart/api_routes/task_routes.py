from flask import Blueprint, request

from stuart.api_core.task_core_api import TaskCoreAPI


class TaskRoutes(object):

    task_blueprint = Blueprint(
        'tasks',
        __name__,
        url_prefix="/tasks")

    @staticmethod
    @task_blueprint.route('/<string:task_id>/', methods=['GET'])
    def read_by_id(task_id):
        dictionary = request.args.to_dict()
        dictionary['id'] = task_id
        return TaskCoreAPI().read(
            filters=dictionary)

    @staticmethod
    @task_blueprint.route('/', methods=['GET'])
    def read_all():
        dictionary = request.args.to_dict()
        return TaskCoreAPI().read(
            filters=dictionary)

    @staticmethod
    @task_blueprint.route('/', methods=['PUT'])
    def create():
        return TaskCoreAPI().create(request)

    @staticmethod
    @task_blueprint.route('/<string:task_id>/', methods=['DELETE'])
    def delete(task_id):
        dictionary = request.args.to_dict()
        dictionary['id'] = task_id
        return TaskCoreAPI().delete(
            filters=dictionary)

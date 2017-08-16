from flask import Blueprint, request

from stuart.api_core.task_event_core_api import TaskEventCoreAPI


class TaskEventRoutes(object):

    task_events_blueprint = Blueprint(
        'task_events',
        __name__,
        url_prefix="/task_events")

    @staticmethod
    @task_events_blueprint.route('/<string:task_event_id>/', methods=['GET'])
    def read_by_id(task_event_id):
        dictionary = request.args.to_dict()
        dictionary['id'] = task_event_id
        return TaskEventCoreAPI().read(
            filters=dictionary)

    @staticmethod
    @task_events_blueprint.route('/', methods=['GET'])
    def read_all():
        dictionary = request.args.to_dict()
        return TaskEventCoreAPI().read(
            filters=dictionary)

    @staticmethod
    @task_events_blueprint.route('/', methods=['PUT'])
    def create():
        return TaskEventCoreAPI().create(request)

    @staticmethod
    @task_events_blueprint.route('/<string:task_event_id>/', methods=['DELETE'])
    def delete(task_event_id):
        dictionary = request.args.to_dict()
        dictionary['id'] = task_event_id
        return TaskEventCoreAPI().delete(
            filters=dictionary)

from flask import Flask
from flask_cors import CORS

from stuart.database.database import db
from stuart.path_utils import get_app_base_path


def create_app():

    app = Flask(__name__, instance_path=get_app_base_path())
    app.config.from_object("stuart.config.DevelopmentConfig")

    from stuart.api_routes.module_routes import ModuleRoutes
    from stuart.api_routes.action_routes import ActionRoutes
    from stuart.api_routes.task_routes import TaskRoutes
    from stuart.models.generic_params_patterns import GenericParamsPatterns
    from stuart.models.params_dictionary import ParamsDictionaries
    from stuart.api_routes.user_task_routes import UserTaskRoutes
    from stuart.api_routes.task_event_routes import TaskEventRoutes

    app.register_blueprint(ModuleRoutes.module_blueprint)
    app.register_blueprint(ActionRoutes.action_blueprint)
    app.register_blueprint(TaskRoutes.task_blueprint)
    app.register_blueprint(UserTaskRoutes.user_task_blueprint)
    app.register_blueprint(TaskEventRoutes.task_events_blueprint)

    CORS(app)
    db.init_app(app)

    return app

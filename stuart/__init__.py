from flask import Flask
from flask_cors import CORS

from stuart.database.database import db
from stuart.path_utils import get_app_base_path


def create_app():

    app = Flask(__name__, instance_path=get_app_base_path())
    app.config.from_object("stuart.config.DevelopmentConfig")

    from stuart.api.module_api import ModuleAPI
    from stuart.api.action_api import ActionAPI

    app.register_blueprint(ModuleAPI.module_blueprint)
    app.register_blueprint(ActionAPI.action_blueprint)

    CORS(app)
    db.init_app(app)

    return app

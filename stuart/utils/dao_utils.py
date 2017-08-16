import sys

from flask import current_app


def get_dao_with_model_name(model_name):
    try:
        service_class = str(model_name.title() + 'DAO')
        return getattr(sys.modules['stuart.dao'], service_class)()
    except AttributeError as err:
        current_app.logger.error(err.args[0])
        sys.exit()

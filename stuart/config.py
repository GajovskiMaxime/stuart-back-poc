import os

import logging

from flask import config

from stuart.path_utils import get_folder_path_from_root_project


class BaseConfig:

    """Base configuration"""

    def __init__(self):
        pass

    DEBUG = False
    TESTING = False

    # Database
    DB_NAME = 'database.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + get_folder_path_from_root_project("database" + os.path.sep) + DB_NAME + '?check_same_thread=False'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing configuration"""
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False


def configure_app(app):

    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[config_name])

    # Configure logging
    handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
    handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)


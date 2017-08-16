import os
import subprocess
import sys
import unittest

from flask import current_app, json
from flask_script import Manager

from stuart import create_app
from stuart.database.database import db
from stuart.exceptions.file.file_exception import FileException
from stuart.path_utils import get_folder_path_from_root_project
from stuart.utils.csv_utils import module_csv_to_sql, action_csv_to_sql

app = create_app()
manager = Manager(app)


@manager.command
def test():
    """Runs the tests without code coverage."""
    current_app.logger.info(get_folder_path_from_root_project('tests'))
    tests = unittest.TestLoader().discover(
        get_folder_path_from_root_project('tests'),
        pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def delete_database():
    """Deletes the current database into stuart/database/*.db"""
    path_to_database = get_folder_path_from_root_project("database" + os.path.sep + app.config['DB_NAME'])
    if not os.path.exists(path_to_database):
        current_app.logger.warning("Database at {} doesn't exist.".format(path_to_database))
        return
    try:
        current_app.logger.info("Deleting database at {}".format(path_to_database))
        subprocess.check_output(
            "rm -rf " + get_folder_path_from_root_project("database" + os.path.sep + "database.db"),
            stderr=subprocess.STDOUT, shell=True,
            universal_newlines=True)
    except subprocess.CalledProcessError:
        current_app.logger.error("Another program is currently using the database.")
        sys.exit()


@manager.command
def recreate_database():
    """Recreates the database : drop_all() and create_all()"""
    current_app.logger.info("Recreating database.")
    db.drop_all()
    db.create_all()


# TODO I actually use services but there's no control for session rollback.
# TODO If I use DAO there's no way to control inputs.
@manager.command
def populate_database():
    """Populates the database with csv files into stuart/csv/*.csv"""
    current_app.logger.info("Populating the database.")
    try:
        module_csv_to_sql()
        action_csv_to_sql()
    except FileException as f:
        current_app.logger.error(json.dumps(f.serialize))
        exit()


@manager.command
def reset_database():
    delete_database()
    recreate_database()
    populate_database()


if __name__ == '__main__':
    manager.run()

from flask import current_app
from numpy import genfromtxt

from stuart import create_app
from stuart.exceptions.file.file_format_exception import FileFormatException
from stuart.exceptions.file.file_not_found_exception import FileNotFoundException
from stuart.models.action import Action
from stuart.models.module import Module
from stuart.path_utils import get_csv_path_from_table_name
from stuart.utils.service_utils import get_service_with_model_name


def load_data(file_name):
    data = genfromtxt(
        file_name,
        delimiter=';',
        skip_header=1,
        missing_values='',
        filling_values='',
        dtype=None)

    return data.tolist()


# TODO : Need refacto. for csv_to_sql methods.
# TODO : Not important atm.
def module_csv_to_sql():

    with create_app().app_context():
        file_path = None
        try:
            service = get_service_with_model_name(
                model_name=Module.table_name())

            file_path = get_csv_path_from_table_name(Module.table_name())
            current_app.logger.info("Opening file : {}.".format(file_path))
            data = load_data(file_path)
            current_app.logger.info("{} rows found on file.".format(sum(1 for row in data)))

            for attr in data:
                module_dict = {
                    'label':        attr[0].decode('utf-8'),
                    'command':      attr[1].decode('utf-8'),
                    'is_preset':    True
                }
                service.create(
                    autocommit=True,
                    args=module_dict)

                current_app.logger.info("Rows inserted successfully.")
        except (IndexError, ValueError) as err:
            raise FileFormatException(
                file_path=file_path,
                err=err.args[0])
        except OSError as err:
            if '.csv not found' in err.args[0]:
                raise FileNotFoundException(
                    file_path=file_path,
                    err=err.args[0])


def action_csv_to_sql():
    with create_app().app_context():
        file_path = None
        try:
            action_service = get_service_with_model_name(
                model_name=Action.table_name())

            module_service = get_service_with_model_name(
                model_name=Module.table_name())

            file_path = get_csv_path_from_table_name(Action.table_name())
            current_app.logger.info("Opening file : {}.".format(file_path))
            data = load_data(file_path)
            current_app.logger.info("{} rows found on file.".format(sum(1 for row in data)))
            current_module = None
            for attr in data:
                if not current_module or current_module.label != attr[0].decode('utf-8'):
                    current_app.logger.info(attr[0].decode('utf-8'))
                    current_module = module_service.read(
                            filters={'label': attr[0].decode('utf-8')},
                            mode='exact')[0]

                dict_from_attr = {
                    'module':       current_module.id,
                    'category':     attr[1].decode('utf-8'),
                    'label':        attr[2].decode('utf-8'),
                    'command':      attr[3].decode('utf-8'),
                    'is_preset':    True
                }

                action_service.create(
                    autocommit=True,
                    args=dict_from_attr)

            current_app.logger.info("Rows inserted successfully.")
        except (IndexError, ValueError) as err:
            raise FileFormatException(
                file_path=file_path,
                err=err.args[0])
        except OSError as err:
            if '.csv not found' in err.args[0]:
                raise FileNotFoundException(
                    file_path=file_path,
                    err=err.args[0])

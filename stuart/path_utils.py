import os


def get_app_base_path():
    return os.path.dirname(os.path.realpath(__file__))


def get_folder_path_from_root_project(path):
    return os.path.join(get_app_base_path(), path)


def get_csv_path_from_table_name(table_name):
    return get_folder_path_from_root_project(
        "csv" + os.path.sep + table_name + ".csv")

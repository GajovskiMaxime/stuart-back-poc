import subprocess

from flask import current_app, json

from stuart import create_app
from stuart.api_core.generic_core_api import GenericCoreAPI
from stuart.database.database import get_session
from stuart.services import ModuleService
from stuart.services.user_task_services import UserTaskService


class UserTaskCoreAPI(GenericCoreAPI):
    """
          User Task Core API class.
          -----------------
          :extends: GenericCoreAPI
          :service: UserTaskService
      """
    def __init__(self):
        super(UserTaskCoreAPI, self).\
            __init__(service=UserTaskService)

    def execute(self, filters):
        with create_app().app_context():
            try:
                user_task = self._service.read(
                    filters=filters,
                    mode='exact')[0]

                current_app.logger.info(user_task.serialize)

                args_pattern = user_task.task_relation.task_params_relation.generic_params_patterns_relation.generic_args_pattern
                target_pattern = user_task.task_relation.task_params_relation.generic_params_patterns_relation.generic_target_pattern

                filled_args = args_pattern.format(**json.loads(user_task.params_dictionaries_relation.args_dictionary))
                filled_target = target_pattern.format(**json.loads(user_task.params_dictionaries_relation.target_dictionary))

                module = ModuleService().read(
                    filters={'id': user_task.task_relation.action_relation.module},
                    mode='exact')[0]

                output = subprocess.check_output(
                    module.command + ' ' + filled_target + ' ' + user_task.task_relation.action_relation.command + ' ' + filled_args,
                    shell=True,
                    stderr=subprocess.STDOUT,
                    universal_newlines=True)
                current_app.logger.info(output)

            except subprocess.CalledProcessError as processError:
                output = processError.output
                current_app.logger.info(output)

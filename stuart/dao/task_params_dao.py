from stuart.dao.abstract_generic_dao import AbstractGenericDAO
from stuart.models.task_params import TaskParams


class TaskParamsDAO(AbstractGenericDAO):

    def __init__(self):
        super(TaskParamsDAO, self).__init__(
            table=TaskParams)

    def create(self, session, model):
        return super(TaskParamsDAO, self).create(
            session=session,
            model=model)

    def read_all(self, session, filters):
        return super(TaskParamsDAO, self).read_all(
            session=session,
            filters=filters)

    def delete(self, session, filters):
        return super(TaskParamsDAO, self).delete(
            session=session,
            filters=filters)

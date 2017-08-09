from sqlalchemy import UniqueConstraint

from stuart.database.database import db
from stuart.models.abstract_model import AbstractModel
from stuart.models_properties.user_task_properties import UserTaskProperties


class UserTask(db.Model, AbstractModel):

    __tablename__ = 'USER_TASK'

    _properties = UserTaskProperties()

    # --------- Columns ---------

    id = db.Column(
        **_properties.get_sql_attr_column('id'))

    task = db.Column(
        db.ForeignKey('TASK.ID'),
        **_properties.get_sql_attr_column('task'))

    params_dictionaries = db.Column(
        db.ForeignKey('PARAMS_DICTIONARIES.ID'),
        **_properties.get_sql_attr_column('params_dictionaries'))

    created_at = db.Column(
        **_properties.get_sql_attr_column('created_at'))

    # --------- Relationships ---------

    params_dictionaries_relation = db.relationship(
        **_properties.get_relation('params_dictionaries'))

    task_relation = db.relationship(
        **_properties.get_relation('task'))

    # --------- Constraints ---------

    UniqueConstraint(task, params_dictionaries)

    def __init__(self, task, params_dictionaries):
        super().__init__()
        self.task = task
        self.params_dictionaries = params_dictionaries

    # --- Display functions ---

    @property
    def serialize(self):
        lazy_dict = self.serialize_lazy
        lazy_dict['task'] = self.task_relation.serialize
        lazy_dict['params_dictionaries'] = self.params_dictionaries_relation.serialize
        return lazy_dict

    @property
    def serialize_lazy(self):
        return {
            'id':                   self.id,
            'task':                 self.task,
            'params_dictionaries':  self.params_dictionaries,
            'created_at':           self.created_at,
        }
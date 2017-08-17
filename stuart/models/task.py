
from sqlalchemy import UniqueConstraint

from stuart.database.database import db
from stuart.models.abstract_model import AbstractModel
from stuart.models_properties.task_properties import TaskProperties


class Task(db.Model, AbstractModel):

    __tablename__ = 'TASK'

    _properties = TaskProperties()

    # --------- Columns ---------

    id = db.Column(
        **_properties.get_sql_attr_column('id'))

    action = db.Column(
        db.ForeignKey('ACTION.ID'),
        **_properties.get_sql_attr_column('action'))

    task_params = db.Column(
        db.ForeignKey('TASK_PARAMS.ID'),
        **_properties.get_sql_attr_column('task_params'))

    custom_label = db.Column(
        **_properties.get_sql_attr_column('custom_label'))

    created_at = db.Column(
        **_properties.get_sql_attr_column('created_at'))

    # --------- Relationships ---------

    task_params_relation = db.relationship(
        **_properties.get_relation('task_params'))

    action_relation = db.relationship(
        **_properties.get_relation('action'))

    # --------- Constraints ---------

    UniqueConstraint(action, task_params)

    def __init__(self, action, task_params, custom_label=""):
        super().__init__()
        self.custom_label = custom_label
        self.action = action
        self.task_params = task_params

    # --- Display functions ---

    @property
    def serialize(self):
        lazy_dict = self.serialize_lazy
        lazy_dict['task_params'] = self.task_params_relation.serialize
        return lazy_dict

    @property
    def serialize_lazy(self):
        return {
            'id':           self.id,
            'action':       self.action,
            'custom_label': self.custom_label,
            'task_params':  self.task_params,
            'created_at':   self.created_at,
        }

    def __repr__(self):
        return '{} : {}'.format(self.table_name(), self.serialize_lazy)

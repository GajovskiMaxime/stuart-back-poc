
from sqlalchemy import UniqueConstraint

from stuart.models.utils import get_mandatory_fields_for_post, get_columns_labels
from stuart.database.database import db
from stuart.models_properties.task_properties import TaskProperties


class Task(db.Model):

    __tablename__ = 'TASK'

    properties = TaskProperties()

    # --------- Columns ---------

    id = db.Column(
        **properties.get_sql_attr_column('id'))

    action_id = db.Column(
        db.ForeignKey('ACTION.ID'),
        **properties.get_sql_attr_column('action_id'))

    task_params_id = db.Column(
        db.ForeignKey('TASK_PARAMS.ID'),
        **properties.get_sql_attr_column('task_params_id'))

    custom_label = db.Column(
        **properties.get_sql_attr_column('custom_label'))

    created_at = db.Column(
        **properties.get_sql_attr_column('created_at'))

    # --------- Relationships ---------

    task_params = db.relationship(**properties.get_relation('task_params'))

    # --------- Constraints ---------

    UniqueConstraint(action_id, task_params_id)

    def __init__(self, custom_label, action_id, task_params_id):
        self.custom_label = custom_label
        self.action_id = action_id
        self.task_params_id = task_params_id

    # --- Display functions ---

    @property
    def serialize(self):
        lazy_dict = self.serialize_lazy
        lazy_dict['task_params'] = self.task_params.serialize
        return lazy_dict

    @property
    def serialize_lazy(self):
        return {
            'id':           self.id,
            'action':       self.action_id,
            'custom_label': self.custom_label,
            'task_params':  self.task_params_id,
            'created_at':   self.created_at,
        }

    def __repr__(self):
        return '{} : {}'.format(self.table_name(), self.serialize_lazy)

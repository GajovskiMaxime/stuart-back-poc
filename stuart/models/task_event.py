from stuart.database.database import db
from stuart.models.abstract_model import AbstractModel
from stuart.models_properties.task_event_properties import TaskEventProperties


class TaskEvent(db.Model, AbstractModel):

    __tablename__ = 'TASK_EVENT'

    _properties = TaskEventProperties()

    id = db.Column(
        **_properties.get_sql_attr_column('id'))

    user_task = db.Column(
        db.ForeignKey('USER_TASK.ID'),
        **_properties.get_sql_attr_column('user_task'))

    begin = db.Column(
        **_properties.get_sql_attr_column('begin'))

    end = db.Column(
        **_properties.get_sql_attr_column('end'))

    status = db.Column(
        **_properties.get_sql_attr_column('status'))

    # --------- Relationships ---------
    user_task_relation = db.relationship(
        **_properties.get_relation('user_task'))

    def __init__(self, user_task):
        super().__init__()
        self.user_task = user_task

    # --- Display functions ---

    @property
    def serialize(self):
        lazy_dict = self.serialize_lazy
        return lazy_dict

    @property
    def serialize_lazy(self):
        return {
            'id':           self.id,
            'user_task':    self.user_task,
            'begin':        self.begin,
            'end':          self.end,
            'status':       self.status,
        }
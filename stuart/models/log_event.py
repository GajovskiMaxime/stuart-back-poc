from stuart.database.database import db
from stuart.models.abstract_model import AbstractModel
from stuart.models_properties.log_event_properties import LogEventProperties


class LogEvent(db.Model, AbstractModel):

    __tablename__ = 'LOG_EVENT'

    _properties = LogEventProperties()

    id = db.Column(
        **_properties.get_sql_attr_column('id'))

    task_event = db.Column(
        db.ForeignKey('TASK_EVENT.ID'),
        **_properties.get_sql_attr_column('task_event'))

    status_code = db.Column(
        **_properties.get_sql_attr_column('status_code'))

    stderr = db.Column(
        **_properties.get_sql_attr_column('stderr'))

    stdout = db.Column(
        **_properties.get_sql_attr_column('stdout'))

    # --------- Relationships ---------
    task_event_relation = db.relationship(
        **_properties.get_relation('task_event'))

    def __init__(self, task_event):
        super().__init__()
        self.task_event = task_event

    # --- Display functions ---

    @property
    def serialize(self):
        lazy_dict = self.serialize_lazy
        return lazy_dict

    @property
    def serialize_lazy(self):
        return {
            'id':           self.id,
            'task_event':   self.task_event,
            'status_code':  self.status_code,
            'stdout':       self.stdout,
            'stderr':       self.stderr,
        }

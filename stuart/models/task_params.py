from sqlalchemy import UniqueConstraint

from stuart.database.database import db

from stuart.models.abstract_model import AbstractModel


class TaskParams(db.Model, AbstractModel):

    __tablename__ = 'TASK_PARAMS'

    _properties = TaskParamsProperties()

    # --------- Columns ---------

    id = db.Column(
        **_properties.get_column('id'))

    params_patterns_id = db.Column(
        db.ForeignKey('PARAMS_PATTERNS.ID'),
        **_properties.get_column('params_patterns_id'))

    params_dictionaries_id = db.Column(
        db.ForeignKey('PARAMS_DICTIONARIES.ID'),
        **_properties.get_column('params_dictionaries_id'))

    # --------- Relationships ---------

    params_patterns = db.relationship(**_properties.get_relation('params_patterns'))
    params_dictionaries = db.relationship(**_properties.get_relation('params_dictionaries'))

    # --------- Constraints ---------

    UniqueConstraint(params_patterns_id, params_dictionaries_id)

    def __init__(self, params_patterns_id, params_dictionaries_id):
        super().__init__()
        self.params_patterns_id = params_patterns_id
        self.params_dictionaries_id = params_dictionaries_id

    # --- Display functions ---

    @property
    def serialize(self):
        lazy_dict = self.serialize_lazy
        lazy_dict['params_patterns'] = self.params_patterns.serialize_lazy
        lazy_dict['params_dictionaries'] = self.params_dictionaries.serialize_lazy
        return lazy_dict

    @property
    def serialize_lazy(self):
        return {
            'id':                       self.id,
            'params_patterns':       self.params_patterns_id,
            'params_dictionaries':   self.params_dictionaries_id
        }

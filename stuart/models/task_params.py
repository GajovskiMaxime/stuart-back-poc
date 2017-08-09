from sqlalchemy import UniqueConstraint

from stuart.database.database import db

from stuart.models.abstract_model import AbstractModel
from stuart.models_properties.task_params_properties import TaskParamsProperties


class TaskParams(db.Model, AbstractModel):

    __tablename__ = 'TASK_PARAMS'

    _properties = TaskParamsProperties()

    # --------- Columns ---------

    id = db.Column(
        **_properties.get_sql_attr_column('id'))

    generic_params_patterns = db.Column(
        db.ForeignKey('GENERIC_PARAMS_PATTERNS.ID'),
        **_properties.get_sql_attr_column('generic_params_patterns'))

    params_dictionaries = db.Column(
        db.ForeignKey('PARAMS_DICTIONARIES.ID'),
        **_properties.get_sql_attr_column('params_dictionaries'))

    # --------- Relationships ---------

    generic_params_patterns_relation = db.relationship(
        **_properties.get_relation('generic_params_patterns'))

    params_dictionaries_relation = db.relationship(
        **_properties.get_relation('params_dictionaries'))

    # --------- Constraints ---------

    UniqueConstraint(generic_params_patterns, params_dictionaries)

    def __init__(self, generic_params_patterns, params_dictionaries):
        super().__init__()
        self.generic_params_patterns = generic_params_patterns
        self.params_dictionaries = params_dictionaries

    # --- Display functions ---

    @property
    def serialize(self):
        lazy_dict = self.serialize_lazy
        lazy_dict['generic_params_patterns'] = self.\
            generic_params_patterns_relation\
            .serialize_lazy

        lazy_dict['params_dictionaries'] = self.params_dictionaries_relation\
            .serialize_lazy
        return lazy_dict

    @property
    def serialize_lazy(self):
        return {
            'id':                       self.id,
            'generic_params_patterns':  self.generic_params_patterns,
            'params_dictionaries':      self.params_dictionaries
        }

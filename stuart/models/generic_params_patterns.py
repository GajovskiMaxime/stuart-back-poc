from sqlalchemy import UniqueConstraint

from stuart.database.database import db
from stuart.models.abstract_model import AbstractModel
from stuart.models_properties.generic_params_patterns_properties import GenericParamsPatternsProperties


class GenericParamsPatterns(db.Model, AbstractModel):

    __tablename__ = 'GENERIC_PARAMS_PATTERNS'

    _properties = GenericParamsPatternsProperties()

    # --------- Columns ---------

    id = db.Column(
        **_properties.get_column('id'))

    generic_args_pattern = db.Column(
        **_properties.get_column('args_pattern'))

    generic_target_pattern = db.Column(
        **_properties.get_column('target_pattern'))

    # --------- Constraints ---------

    UniqueConstraint(generic_args_pattern, generic_target_pattern)

    # --------- Constructor ---------

    def __init__(self, generic_args_pattern, generic_target_pattern):
        super().__init__()

        self.generic_args_pattern = generic_args_pattern
        self.generic_target_pattern = generic_target_pattern

    # --- Display functions ---

    @property
    def serialize(self):
        lazy_dict = self.serialize_lazy
        return lazy_dict

    @property
    def serialize_lazy(self):
        return {
            'id':                       self.id,
            'generic_args_pattern':     self.generic_args_pattern,
            'generic_target_pattern':   self.generic_target_pattern
        }

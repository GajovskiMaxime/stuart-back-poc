from sqlalchemy import UniqueConstraint

from stuart.database.database import db

from stuart.models.abstract_model import AbstractModel
from stuart.models_properties.action_properties import ActionProperties


class Action(db.Model, AbstractModel):

    __tablename__ = 'ACTION'

    _properties = ActionProperties()

    # --------- Columns ---------

    id = db.Column(
        **_properties.get_sql_attr_column('id'))

    module = db.Column(
        db.ForeignKey('MODULE.ID'),
        **_properties.get_sql_attr_column('module'))

    category = db.Column(
        **_properties.get_sql_attr_column('category'))

    label = db.Column(
        **_properties.get_sql_attr_column('label'))

    command = db.Column(
        **_properties.get_sql_attr_column('command'))

    is_tested = db.Column(
        **_properties.get_sql_attr_column('is_tested'))

    is_preset = db.Column(
        **_properties.get_sql_attr_column('is_preset'))

    # --------- Constraints ---------

    UniqueConstraint(module, command)

    # --------- Constructor ---------

    def __init__(self, module, label, command,
                 category='', is_preset=False, is_tested=False):
        super(Action, self).__init__()

        self.module = module
        self.category = category
        self.label = label
        self.command = command
        self.is_tested = is_tested
        self.is_preset = is_preset

    # --- Display functions ---

    @property
    def serialize(self):
        lazy_dict = self.serialize_lazy
        return lazy_dict

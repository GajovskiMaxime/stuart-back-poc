from stuart.database.database import db

from stuart.models.abstract_model import AbstractModel
from stuart.models_properties.action_properties import ActionProperties


class Action(db.Model, AbstractModel):

    __tablename__ = 'ACTION'

    _properties = ActionProperties()

    # --------- Columns ---------

    id = db.Column(
        **_properties.get_column('id'))

    module_id = db.Column(
        db.ForeignKey('MODULE.ID'),
        **_properties.get_column('module_id'))

    category = db.Column(
        **_properties.get_column('category'))

    label = db.Column(
        **_properties.get_column('label'))

    command = db.Column(
        **_properties.get_column('command'))

    is_tested = db.Column(
        **_properties.get_column('is_tested'))

    is_preset = db.Column(
        **_properties.get_column('is_preset'))

    # --------- Constraints ---------
    # TODO : Needed constraints

    def __init__(self, module_id, label, command,
                 category='', is_preset=False, is_tested=False):
        super(Action, self).__init__()

        self.module_id = module_id
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

    @property
    def serialize_lazy(self):
        return {
            'id':            self.id,
            'module_id':     self.module_id,
            'category':      self.category,
            'label':         self.label,
            'command':       self.command,
            'is_tested':     self.is_tested,
            'is_preset':     self.is_preset
        }

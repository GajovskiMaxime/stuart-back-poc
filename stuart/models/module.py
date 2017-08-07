from stuart.models.abstract_model import AbstractModel
from stuart.database.database import db
from stuart.models_properties.module_properties import ModuleProperties
from stuart.utils.json_utils import list_to_json


class Module(db.Model, AbstractModel):

    __tablename__ = 'MODULE'

    _properties = ModuleProperties()

    # --------- Columns ---------

    id = db.Column(
        **_properties.get_column('id'))

    label = db.Column(
        **_properties.get_column('label'))

    command = db.Column(
        **_properties.get_column('command'))

    is_preset = db.Column(
        **_properties.get_column('is_preset'))

    # --------- Relationships ---------

    actions = db.relationship(**_properties.get_relation('actions'))

    # --------- Constraints ---------
    # TODO : Needed constraints

    def __init__(self, label, command, is_preset=False):
        super(Module, self).__init__()

        self.label = label
        self.command = command
        self.is_preset = is_preset

    # --- Display functions ---

    @property
    def serialize(self):
        lazy_dict = self.serialize_lazy
        # lazy_dict['actions'] = list_to_json(self.actions)
        return lazy_dict

    @property
    def serialize_lazy(self):
        return super(Module, self).serialize_lazy

from flask import json
from sqlalchemy import UniqueConstraint

from stuart.database.database import db
from stuart.models.abstract_model import AbstractModel
from stuart.models_properties.params_dictionaries_properties import ParamsDictionariesProperties


class ParamsDictionaries(db.Model, AbstractModel):

    __tablename__ = 'PARAMS_DICTIONARIES'

    _properties = ParamsDictionariesProperties()

    # --------- Columns ---------

    id = db.Column(
        **_properties.get_sql_attr_column('id'))

    args_dictionary = db.Column(
        **_properties.get_sql_attr_column('args_dictionary'))

    target_dictionary = db.Column(
        **_properties.get_sql_attr_column('target_dictionary'))

    # --------- Constraints ---------

    UniqueConstraint(args_dictionary, target_dictionary)

    # --------- Constructor ---------

    def __init__(self, args_dictionary, target_dictionary):
        super().__init__()

        self.args_dictionary = args_dictionary
        self.target_dictionary = target_dictionary

    # --- Display functions ---

    @property
    def serialize(self):
        serialized_dict = self.serialize_lazy
        return serialized_dict

    @property
    def serialize_lazy(self):
        return {
            'id':                   self.id,
            'args_dictionary':      json.loads(self.args_dictionary),
            'target_dictionary':    json.loads(self.target_dictionary)
        }

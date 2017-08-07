
class AbstractModel(object):

    _properties = None
    __tablename__ = None

    def __init__(self):
        self.id = None

    @classmethod
    def properties(cls):
        return cls._properties

    @classmethod
    def table_name(cls):
        return cls.__tablename__.lower()

    @classmethod
    def mandatory_fields(cls):
        columns = cls.properties().get_columns()
        columns.pop('id', None)

        for k_column, v_column in columns.items():
            if 'nullable' not in v_column \
                    or v_column['nullable'] is True\
                    or 'default' in v_column:
                columns.pop(k_column, None)
        return columns


    @property
    def serialize_lazy(self):
        lazy_dict = {}
        for column in self._properties.get_columns():
            lazy_dict[column] = self.__getattribute__(column)
        return lazy_dict

    def __repr__(self):
        return '{} : {} '.format(self.__tablename__, self.serialize_lazy)

    def __eq__(self, other):
        """Override the default Equals behavior"""
        if not isinstance(other, self.__class__):
            return False
        return self.id == other.id

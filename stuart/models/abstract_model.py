
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

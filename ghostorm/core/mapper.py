from ghostorm.core.instrumented_attribute import InstrumentedAttribute
from ghostorm.core.column import Column
from ghostorm.core.table import Table


class Mapper:
    def __init__(self, cls):
        self.class_ = cls
        self.table_name = cls.__name__.lower()
        self.primary_keys = []
        self.relationships = {}
        self.table = Table(self.table_name)
        self.columns = self.table.columns
        self.scan_class()

    
    def scan_class(self):
        for name, obj in self.class_.__dict__.items():
            if isinstance(obj, Column):
                self.table.add_column(name, obj)
                if obj.primary_key:
                    self.primary_keys.append(obj)
                descriptor = InstrumentedAttribute(obj)
                setattr(self.class_, name, descriptor)

    def load(self, row):
        obj = self.class_()
        for key, value in row.items():
            setattr(obj, key, value)

        return obj
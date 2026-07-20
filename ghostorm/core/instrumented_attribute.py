from ghostorm.core import column


class InstrumentedAttribute:
    def __init__(self, column):
        self.column = column
        self.key = column.name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.key, None)

    def __set__(self, instance, value):
        instance.__dict__[self.key] = value



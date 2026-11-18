from ghostorm.core.registry import registry
from ghostorm.core.instrumented_list import InstrumentedList


class RelationshipProperty:
    def __init__(self, argument, back_populates=None, uselist=None):
        self.argument = argument
        self.back_populates = back_populates
        self.name = None
        self.target_class = None

    def __set_name__(self, owner, name):
        self.name = name

    def resolve(self):
        self.target_class = registry.resolve(self.argument)
        return self.target_class

    def __get__(self, instance, owner):
        if instance is None:
            return self

        if self.name not in instance.__dict__:
            if self.uselist:
                instance.__dict__[self.name] = InstrumentedList(instance, self)
            else:
                instance.__dict__[self.name] = None
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.uselist:
            raise AttributeError(f"cannot directly assign to collection{self.name} use append() instead.  ")
        instance.__dict__[self.name] = value

        if value is not None and self.back_populates:
            reverse = getattr(type(value), self.back_populates)
            collection = getattr(value, self.back_populates)

            if reverse.uselist and instance not in collection:
                collection.append(instance)
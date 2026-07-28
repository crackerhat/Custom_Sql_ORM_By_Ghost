
class InstrumentedAttribute:
    def __init__(self, column):
        self.column = column
        self.key = column.name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.key, None)

    def __set__(self, instance, value):
        # old_value = instance.__dict__.get(self.key)
        attribute_state = instance._state.get_attribute_state(self.key)
        attribute_state.set_value(value)
        instance.__dict__[self.key] = value
        if attribute_state.modified:
            instance._state.mark_dirty()


            if instance._state.session:
                instance._state.session.mark_dirty(instance)



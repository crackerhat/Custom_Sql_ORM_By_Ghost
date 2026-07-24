from ghostorm.orm.attribute_state import AttributeState
class InstanceState:
    def __init__(self, instance):
        self.instance = instance
        self.dirty = False
        self.attributes = {}
        self.mapper = None
        self.session = None
        self.identity = None
    def mark_dirty(self):
        self.dirty = True

    def mark_clean(self):
        self.dirty = False



    def get_attribute_state(self, key):
        if key not in self.attributes:
            self.attributes[key] = AttributeState()
        return self.attributes[key]

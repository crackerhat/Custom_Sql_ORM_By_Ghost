from ghostorm.orm.identity_map import IdentityMap
class Session:
    def __init__(self):
        self.new = []
        self.dirty = []
        self.deleted = []
        self.identity_map = IdentityMap()

    def add(self, instance):
        if instance not in self.new:
            self.new.append(instance)
            instance._state.session = self
            self.identity_map.add(instance)
    def mark_dirty(self, instance):
        if instance in self.new:
            return


        if instance not in self.dirty:
            self.dirty.append(instance)

session = Session()
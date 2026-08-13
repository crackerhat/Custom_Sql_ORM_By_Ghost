from ghostorm.orm.identity_map import IdentityMap
from ghostorm.engine.engine import Engine
from ghostorm.core.registry import registry

class Session:
    def __init__(self):
        self.new = []
        self.dirty = []
        self.deleted = []
        self.identity_map = IdentityMap()
        self.engine = Engine()


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

    def get(self, cls, primary_key):
        try:
            obj = self.identity_map.get(cls, primary_key)
            return obj
        except KeyError:
            print("object is not in Identity Map")

        mapper = registry.get_mapper(cls)

        row = self.engine.select_by_primary_key(mapper.table_name, primary_key)

        if row is None:
            return None

        obj = mapper.load(row)

        self.identity_map.add(obj)

        obj._state.session = self

        return obj



session = Session()
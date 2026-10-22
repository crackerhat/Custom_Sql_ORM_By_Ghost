from ghostorm.orm.identity_map import IdentityMap
from ghostorm.engine.modEngine import Engine
from ghostorm.core.registry import registry
from ghostorm.orm.unit_of_work import UnitOfWork
from ghostorm.orm.query import Query



class Session:
    def __init__(self, engine):
        self.new = []
        self.dirty = []
        self.deleted = []
        self.identity_map = IdentityMap()
        self.engine = engine

    def query(self, model):
        return Query(self, model)


    def add(self, instance):
        if instance not in self.new:
            mapper = registry.get_mapper(type(instance).__name__)
            instance._state.mapper = mapper
            self.new.append(instance)
            instance._state.session = self

    def mark_dirty(self, instance):
        if instance in self.new:
            return
        if instance not in self.dirty:
            self.dirty.append(instance)

    def get(self, cls, primary_key):
        obj = self.identity_map.get(cls, primary_key)
        if obj is not None:
            return obj

        mapper = registry.get_mapper(cls.__name__)

        if mapper is None:
            raise ValueError(f" no mapper registered for {cls.__name__}")

        row = self.engine.select_by_primary_key(mapper.table_name, primary_key)

        if row is None:
            return None

        obj = mapper.load(row)

        self.identity_map.add(obj)

        obj._state.session = self

        return obj



    def delete(self, instance):
        if instance in self.new:
            self.new.remove(instance)
            instance._state.session = None
            return
        if instance in self.dirty:
            self.dirty.remove(instance)

        if instance not in self.deleted:
            self.deleted.append(instance)
            
    def commit(self):
        uow = UnitOfWork(self)
        uow.execute()

    def rollback(self):
        for instance in self.dirty.copy():
            instance._state.rollback()
        self.dirty.clear()

        for instance in self.new:
            instance._state.session = None

        self.new.clear()



# session = Session()



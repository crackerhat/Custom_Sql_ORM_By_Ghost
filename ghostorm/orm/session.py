from ghostorm.orm import attribute_state
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

        primary_key_name = mapper.primary_keys[0].name

        sql = (f"SELECT * FROM {mapper.table_name} WHERE {primary_key_name} = ?")
        cursor = self.engine.execute(sql, [primary_key])

        row = cursor.fetchone()
        if row is None:
            return None

        column_names = [column_names[0] for column_names in cursor.description]

        row_data = dict(zip(column_names, row))

        obj = mapper.load(row_data)
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

    def rollback(self):
        for instance in self.dirty.copy():
            instance._state.rollback()
        self.dirty.clear()

        for instance in self.new:
            instance._state.session = None

        self.new.clear()

    def create_snapshot(self): # guys we use this function to restore the orm state if some error happened during execution
            instances = (self.new + self.dirty + self.deleted)
            instances = list(dict.fromkeys(instances))

            snapshot = {
                "new": self.new.copy(),
                "dirty": self.dirty.copy(),
                "deleted": self.deleted.copy(),
                "identity_map": self.identity_map._objects.copy(),
                "instances": {},
            }

            for instance in instances:

                instance_values = { key: value for key, value in instance.__dict__.items() if key != "state"}

                attribute_values = {}

                for key, attribute_state in instance._state.attributes.items():
                    attribute_values[key] = (attribute_state.original, attribute_state.current, attribute_state.modified)

                snapshot["instances"][instance] = {
                    "values": instance_values,
                    "attributes": attribute_values,
                    "dirty": instance._state.dirty,
                    "mapper": instance._state.mapper,
                    "session": instance._state.session,
                    "identity": instance._state.identity,
                }

            return snapshot


    def _restore_snapshot(self, snapshot):
        self.new = snapshot["new"]
        self.dirty = snapshot["dirty"]
        self.deleted = snapshot["deleted"]

        self.identity_map._objects = snapshot["identity_map"]

        for instance, saved_values in snapshot["instances"].items():
            instance_values = saved_values["values"]

            for key in list(instance.__dict__):
                if key != "_state":
                   del instance.__dict__[key]

            instance.__dict__.update(instance_values)
            instance._state.attribtes.clear()

            for key, values in saved_values["attributes"].items():
                attribute_state = instance._state.get_attribute_state(key)
                (attribute_state.original, attribute_state.current, attribute_state.modified) = values

            instance._state.dirty = saved_values["dirty"]
            instance._state.mapper = saved_values["mapper"]
            instance._state.session = saved_values["session"]
            instance._state.identity = saved_values["identity"]

    def commit(self):
        uow = UnitOfWork(self)
        try:
            uow.execute()

            self.engine.connection.commit()
        except Exception:
            self.engine.connection.rollback()  # the reason i do it this way is all works should have to be commited together not independently
            self.rollback()

            raise





# session = Session()



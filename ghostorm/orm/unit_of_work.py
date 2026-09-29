class UnitOfWork:
    def __init__(self, session):
        self.session = session

    def collect_new(self):
        return self.session.new

    def collect_dirty(self):
        return self.session.dirty

    def collect_deleted(self):
        return self.session.deleted


    def collect_changes(self, instance):
        changes = {}
        for key, attribute_state in instance._state.attributes.items():
            if attribute_state.modified:
                changes[key] = attribute_state.current

        return changes

    def create_update_operation(self, instance):
        changes = self.collect_changes(instance)
        operation = {
            "table" : instance._state.mapper.table_name,
            "primary_key" : instance._state.identity[1],
            "changes" : changes
        }
        return operation


    def execute_updates(self):
        for instance in self.collect_dirty().copy():
            operation = self.create_update_operation(instance)
            success = self.session.engine.update(operation["table"], operation["primary_key"], operation["changes"])
            if success:
                instance._state.commit() # we should have to clear the object state because if we don't do this later when we try to change another attribute it will also include and send the previous values again to the database
                self.session.dirty.remove(instance)

    def create_insert_operation(self, instance):
        row = {}
        for key in instance._state.attributes:
            row[key] = getattr(instance, key)

        operation = {
            "table": instance._state.mapper.table_name,
            "row": row
        }
        return operation

    def execute_insert_operation(self):
        for instance in self.collect_new():
            operation = self.create_insert_operation(instance)

            success = self.session.engine.insert(operation["table"], operation["row"])
            if success:
                instance._state.commit()
                instance._state.identity = (type(instance), instance.id)

                self.session.identity_map.add(instance)
                self.session.new.remove(instance)
    def create_delete_operation(self, instance):
        operation = {
            "table": instance._state.mapper.table_name,
            "primary_key": instance._state.identity[1]
        }
        return operation

    def execute_delete_operation(self):
        for instance in self.collect_deleted().copy(): # guys the use of .copy() is that when we delete an instance from the list we delete from the original list but the photocopy of the list will never change the index
            operation = self.create_delete_operation(instance)
            success = self.session.engine.delete(operation["table"], operation["primary_key"])
            if success:
                self.session.identity_map.remove(instance) # guys i removed the instance from the identity map because it might hold the deleted value
                self.session.deleted.remove(instance)
                instance._state.session = None
                instance._state.identity = None

    def execute(self):
        self.execute_insert_operation()
        self.execute_updates()
        self.execute_delete_operation()

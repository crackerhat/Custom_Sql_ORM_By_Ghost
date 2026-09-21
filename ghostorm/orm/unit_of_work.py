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
        for instance in self.collect_dirty():
            operation = self.create_update_operation(instance)
            self.session.engine.update(operation["table"], operation["primary_key"], operation["changes"])

    def show_operations(self):
        print(self.collect_new())
        print(self.collect_dirty())
        print(self.collect_deleted())

        self.execute_updates()

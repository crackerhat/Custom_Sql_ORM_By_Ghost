class Session:
    def __init__(self):
        self.new = []
        self.dirty = []
        self.deleted = []

    def add(self, instance):
        if instance not in self.new:
            self.new.append(instance)
            instance._state.session = self
    def mark_dirty(self, instance):
        if instance in self.new:
            return

        if instance not in self.dirty:
            self.dirty.append(instance)

session = Session()
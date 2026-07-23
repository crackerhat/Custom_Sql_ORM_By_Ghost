class InstanceState:
    def __init__(self, instance):
        self.instance = instance
        self.dirty = False
        self.history = {}
        self.mapper = None
        self.session = None
        self.identity = None
    def mark_dirty(self):
        self.dirty = True

    def mark_clean(self):
        self.dirty = False

    def record_change(self, key, old, new):
        self.history[key] = (old, new)
        self.mark_dirty()

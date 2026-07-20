class InstanceState:
    def __init__(self, instance):
        self.instance = instance
        self.dirty = False
        self.history = {}
        self.mapper = None
        self.session = None
        self.identity = None


from ghostorm.core.registry import registry

class RelationshipProperty:
    def __init__(self, argument):
        self.argument = argument
        self.target_class = None

    def resolve(self):
        self.target_class = registry.resolve(self.argument)
        
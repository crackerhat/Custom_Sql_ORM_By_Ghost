class Registry:
    def __init__(self):
        self.mappers = {}
    def register(self, mapper):
        self.mappers[mapper.class_.__name__] = mapper
    def get_mapper(self, name):
       return self.mappers.get(name)
registry = Registry()

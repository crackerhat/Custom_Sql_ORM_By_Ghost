from ghostorm.core.registry import registry
class Query:
    def __init__(self, session, model):
        self.session = session
        self.model = model

    def all(self):
        mapper = registry.get_mapper(self.model.__name__)
        rows = self.session.engine.select_all(mapper.table_name)
        objects = []

        for row in rows:
            obj = mapper.load(row)
            self.session.identity_map(obj)
            obj._state.session = self.session
            objects.append(obj)

        return objects

    #session.query(user).all()
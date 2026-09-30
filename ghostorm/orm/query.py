from ghostorm.core.registry import registry
from ghostorm.engine.engine import Engine


class Query:
    def __init__(self, session, model):
        self.session = session
        self.model = model
        self.filters = {}

    def all(self):
        mapper = registry.get_mapper(self.model.__name__)
        if self.filters:
            rows = self.session.engine.select_where(mapper.table_name, self.filters)
        else:
            rows  = self.session.engine.select_all(mapper.table_name)

        objects = []

        for row in rows:
            primary_key = row["id"]
            obj = self.session.identity_map.get(self.model, primary_key)

            if obj is None:
                obj = mapper.load(row)
                self.session.identity_map.add(obj)
                obj._state.session = self.session
            objects.append(obj)

        return objects

    def filter_by(self, **kwargs):
        self.filters.update(kwargs)
        return self



    #session.query(user).all()
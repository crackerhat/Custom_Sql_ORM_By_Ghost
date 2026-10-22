from ghostorm.core.registry import registry
from ghostorm.engine.modEngine import Engine
from ghostorm.engine.compiler import Compiler
from ghostorm.orm.expression import BinaryExpression


# Retrieve every user
# users = session.query(User).all()
#
# # Retrieve one user by primary key
# user = session.get(User, 1)
#
# # Filter users
# users = session.query(User).filter(User.age > 18).all()


class Query:
    def __init__(self, session, model):
        self.session = session
        self.model = model
        self.filters = []
        self.compiler = Compiler()

    def all(self):
        mapper = registry.get_mapper(self.model.__name__)
        sql, parameters = self.compiler.compile_select(mapper.table_name, self.filters)
        cursor = self.session.engine.execute(sql, parameters)

        column_names = [column_names[0] for column_names in cursor.description ]

        objects = []
        for row in cursor.fetchall():
            row_data = dict(zip(column_names, row))
            primary_key_name = mapper.primary_keys[0].name
            primary_key_value = row_data[primary_key_name]

            obj = self.session.identity_map.get(self.model, primary_key_value)

            if obj is None:
                obj = mapper.load(row_data)
                obj._state.session = self.session
                self.session.identity_map.add(obj)
            objects.append(obj)

        return objects

        # if self.filters:
        #     rows = self.session.engine.select_where(mapper.table_name, self.filters)
        # else:
        #     rows  = self.session.engine.select_all(mapper.table_name)
        #
        # objects = []
        #
        # for row in rows:
        #     primary_key = row["id"]
        #     obj = self.session.identity_map.get(self.model, primary_key)
        #
        #     if obj is None:
        #         obj = mapper.load(row)
        #         self.session.identity_map.add(obj)
        #         obj._state.session = self.session
        #
        #     objects.append(obj)
        #
        # return objects

    def filter(self, *expressions):
        self.filters.extend(expressions)
        return self

    def filter_by(self, **kwargs):
        expressions = []
        for key, value in kwargs.items():
            column = getattr(self.model, key)
            expressions.append(BinaryExpression(column, '=', value))
        return self.filter(*expressions)


    #session.query(user).all()
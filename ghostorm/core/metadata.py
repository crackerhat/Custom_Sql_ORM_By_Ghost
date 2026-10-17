from ghostorm.engine.dialect import SQLiteDialect

class MetaData:
    def __init__(self):
        self.tables = {}
        self.dialect = SQLiteDialect()

    def register_table(self, table):
        self.tables[table.name] = table

    def create_all(self, engine):
        for table in self.tables.values():
            sql = self.dialect.compile_create_table(table)
            engine.execute(sql)

metadata = MetaData()



class MetaData:
    def __init__(self):
        self.tables = {}

    def register_table(self, table):
        self.tables[table.name] = table

metadata = MetaData()

class Table:
    def __init__(self, name):
        self.name = name
        self.columns = {}

    def add_column(self, name, column):
        column.name = name
        self.columns[name] = column

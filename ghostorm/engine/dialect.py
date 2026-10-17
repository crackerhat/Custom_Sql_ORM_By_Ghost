
class SQLiteDialect:

    def get_column_type(self, column):
        type_name = column.type_.__name__

        if type_name == "Integer":
            return "INTEGER"

        elif type_name == "String":
            return "TEXT"

        raise ValueError(f"Unsupported column typed entered: {type_name}")

    def compile_column(self, column):
        sql = f"{column.name} {self.get_column_type(column)}"

        if column.primary_key:
            sql += " PRIMARY KEY"

        if not column.nullable:
            sql += " NOT NULL"

        return sql

    def compile_create_table(self, table):
        column_definitions = []

        for column in table.columns.values():
            column_sql = self.compile_column(column)
            column_definitions.append(column_sql)

        columns_sql = ", ".join(column_definitions)

        return (f"CREATE TABLE IF NOT EXISTS {table.name} ({columns_sql})")

#  YO GUYS THIS CLASS IS USED TO COLLECT AND CONSTRUCT A DATA THAT NEEDED TO CREATE TABLE 


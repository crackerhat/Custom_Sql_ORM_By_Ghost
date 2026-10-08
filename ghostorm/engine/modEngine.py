class Engine:
    def __init__(self):
        self.database = {
            "user": [
                {
                    "id": 1,
                    "username": "Ghost",
                    "age" : 20
                },
                {
                    "id": 2,
                    "username": "Alice",
                    "age" : 24
                }

            ]
        }

    def matches(self, row, expression):
        column_name = expression.column.key
        actual_value = row.get(column_name)
        expected_value = expression.value

        if expression.operator == "=":
            return actual_value == expected_value

        elif expression.operator == "!=":
            return actual_value != expected_value

        elif expression.operator == ">":
            return actual_value > expected_value

        elif expression.operator == "<":
            return actual_value < expected_value

        elif expression.operator == ">=":
            return actual_value >= expected_value

        elif expression.operator == "<=":
            return actual_value <= expected_value

        else:
            raise ValueError(f"Unknown operator: {expression.operator}" )


    def select_where(self,table_name, expressions):
        rows = self.database.get(table_name, [])
        results = []

        for row in rows:
            matches = True
            for expression in expressions:
               if not self.matches(row, expression):
                    matches = False
                    break

            if matches:
                results.append(row)

        return results


    def select_all(self, table_name):
        return self.database.get(table_name, [])

    def select_by_primary_key(self, table_name, primary_key):


        rows = self.database.get(table_name, [])

        for row in rows:
            if row["id"] == primary_key:
                return row
        print("row not found")

        return None

    def update(self, table_name, primary_key, changes):
        print(f"updating table {table_name}")
        rows = self.database.get(table_name, [])

        for row in rows:
            if row["id"] == primary_key:
                for column, value in changes.items():
                    row[column] = value

                print("row updated sucessfully")
                return True
        print("row not found")
        return False

    def insert(self, table_name, row):
        if table_name not in self.database:
            self.database[table_name] = []
        self.database[table_name].append(row.copy()) #Hey guys the use of using .copy() here is that even if we modify the row later it will not modify the row inside  our mock database

        print(f"inserted successfully")

        return True

    def delete(self, table_name, primary_key):
        print(f"deleting from table {table_name}")
        rows = self.database.get(table_name, [])

        for index, row in enumerate(rows):
            if row["id"] == primary_key:
                rows.pop(index)
                print("deleted successfully")
                return True

        
        print("row not found")
        return False




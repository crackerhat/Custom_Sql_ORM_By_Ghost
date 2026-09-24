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

    def select_by_primary_key(self, table_name, primary_key):

        print(f"searching table {table_name} for id={primary_key}")

        rows = self.database.get(table_name, [])

        for row in rows:
            if row["id"] == primary_key:
                print(" Row Found! ")
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

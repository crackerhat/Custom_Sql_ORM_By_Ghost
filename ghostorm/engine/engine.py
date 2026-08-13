class Engine:
    def __init__(self):
        self.database = {
            "users": [
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
        print("[ENGINE]")
        print(f"searching table {table_name} for id={primary_key}")

        rows = self.database.get(table_name, [])

        for row in rows:
            if row["id"] == primary_key:
                print("[ENGINE] Row Found! ")
                return row
        print("[ENGINE] row not found")

        return None
import sqlite3

class Engine:

    def __init__(self, database_url):
        self.connection = sqlite3.connect(database_url)

    def execute(self, sql, parameters=None):
        cursor = self.connection.cursor()
        cursor.execute(sql, parameters or []) #guys i have set this -> or [] thing to avoid sqlite error i have encountered
        return cursor

    def insert(self, table_name, row):
        columns = list(row.keys())

        if columns:
            column_names = ", ".join(columns)
            question_marks = []

            for _ in columns:
                question_marks.append("?") # guys we have to use quetion marks okay and the reason is to defend hackers from sql injection attack on our website database this is called parametrized query

            placeholders = ", ".join(question_marks)

            sql = (f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})")

            values = [row[column] for column in columns]
        else:
            sql = f"INSERT INTO {table_name} DEFAULT VALUES" # this line is because the database have to automaticallly assign an id value if we don't give the users an id and also the row of the instance is empty this will be triggered 
            values = []

        cursor = self.execute(sql, values)

        return cursor.lastrowid

    def update(self, table_name, primary_key, changes):
        if not changes:
            return True

        assignments = ",".join(f"{column} = ?" for column in changes)

        sql = (f"UPDATE {table_name} SET {assignments} WHERE id = ?")

        values = list(changes.values())
        values.append(primary_key)

        cursor = self.execute(sql, values)


        if cursor.rowcount > 0: # HEY GUYS THIS LINE HERE I ADDED IS  BECAUSE WE HAVE TO KNOW THAT ROW EXISTS AND ALSO WE HAVE TO KNOW IT IS UPDATED
            return True
        else:
            return False

    def delete(self, table_name, primary_key):
        sql = f"DELETE FROM {table_name} WHERE id = ?"
        cursor = self.execute(sql, [primary_key])


        if cursor.rowcount > 0:
            return True
        else:
            return False






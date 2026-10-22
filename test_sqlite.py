# from ghostorm.engine.engine import Engine
#
# engine = Engine("ghostorm.db")
#
# # cursor = engine.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER,  username TEXT, age  INTEGER) ")
# engine.execute("INSERT INTO user (id, username, age) VALUES (?, ?, ?)", [1, "ghostorm", 20])
#
# engine.connection.commit()
#
# cursor = engine.execute("SELECT * FROM user")
#
# rows = cursor.fetchall()
#
# print(rows)
# # print("Database Created")

from ghostorm.core.column import Column
from ghostorm.core.table import Table
from ghostorm.types import Integer, String
from ghostorm.engine.dialect import SQLiteDialect

# table = Table("user")
# table.add_column("id", Column(Integer, primary_key=True))
#
# table.add_column("username", Column(String))
#
# table.add_column("age", Column(Integer))
#
# dialect = SQLiteDialect()
#
# sql = dialect.compile_create_table(table)
#
# print(sql)



from ghostorm.engine.engine import Engine


engine = Engine("ghostorm.db")

# Make sure the table exists first.
engine.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        age INTEGER
    )
""")
engine.connection.commit()

# INSERT
engine.insert("user", {
    "id": 100,
    "username": "GhostORM",
    "age": 19
})

# UPDATE
engine.update("user", 100, {
    "age": 20
})

# DELETE
engine.delete("user", 100)

# Verify the row was deleted.
cursor = engine.execute(
    "SELECT * FROM user WHERE id = ?",
    [100]
)

print("Remaining row:", cursor.fetchone())

engine.connection.close()

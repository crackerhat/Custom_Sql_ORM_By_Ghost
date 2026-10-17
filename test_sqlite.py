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

table = Table("user")
table.add_column("id", Column(Integer, primary_key=True))

table.add_column("username", Column(String))

table.add_column("age", Column(Integer))

dialect = SQLiteDialect()

sql = dialect.compile_create_table(table)

print(sql)
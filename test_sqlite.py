from ghostorm.engine.engine import Engine

engine = Engine("ghostorm.db")

cursor = engine.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER,  username TEXT, age  INTEGER) ")

engine.connection.commit()
print("Database Created")
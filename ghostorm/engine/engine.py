import sqlite3

class Engine:

    def __init__(self, database_url):
        self.connection = sqlite3.connect(database_url)

    def execute(self, sql, parameters=None):
        cursor = self.connection.cursor()
        cursor.execute(sql, parameters or []) #guys i have set this -> or [] thing to avoid sqlite error i have encountered
        return cursor



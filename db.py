import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("app1.db",check_same_thread=False)
        self.cursor = self.connection.cursor()

    def create_table(self):
        sql_command="""CREATE TABLE IF NOT EXISTS user(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        user_name VARCHAR(20),
        password VARCHAR(30)
        );"""

        self.cursor.execute(sql_command)
        self.connection.commit()

    def add_user(self,user_name, password):
        sql_command = """INSERT INTO user (user_name,password)
            VALUES (?,?);"""
        self.cursor.execute(sql_command, (user_name, password))
        self.connection.commit()
        return "Done"

    def get_user(self,user_name):
        sql_command = """SELECT password from user WHERE user_name = ?;"""
        self.cursor.execute(sql_command, (user_name,))
        data = self.cursor.fetchone()
        return data
    def close_connection(self):
        self.connection.close()
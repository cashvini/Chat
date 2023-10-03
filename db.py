import sqlite3


connection = sqlite3.connect('chatty.db')
cursor = connection.cursor()

command = """CREATE TABLE IF NOT EXISTS USER(name TEXT, email TEXT, uname TEXT, password TEXT)"""
cursor.execute(command)

cursor.execute("INSERT INTO user VALUES ('Mala','mala@gmail.com','mala','123')")
cursor.execute("INSERT INTO user VALUES ('Lela','lela@gmail.com','lela','123')")
cursor.execute("INSERT INTO user VALUES ('Kela','kela@gmail.com','kela','123')")
cursor.execute("INSERT INTO user VALUES ('Nela','nela@gmail.com','nela','123')")

connection.commit()

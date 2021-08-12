import sqlite3

con = sqlite3.connect("question.db")
print("Database opened successfully")

con.execute("create table qpaper (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, year INTEGER , link VARCHAR(2083)NOT NULL)")

print("Table created successfully")

con.close()  

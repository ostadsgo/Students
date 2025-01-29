import sqlite3


name = "Joe Doe"
age = 12


# connection
conn = sqlite3.connect("person.db")

# cursor
cur = conn.cursor()
cur.execute("INSERT INTO Student(name,grade) VALUES(?,?)", (name, age))
conn.commit()

conn.close()

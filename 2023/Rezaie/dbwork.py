import sqlite3


conn = sqlite3.connect("students.db")

cursor = conn.cursor()
cursor.execute("SELECT * FROM Student;")
data = cursor.fetchall()
print(data)

total = 0
number_of_std = 0
for row in data:
    total = total + row[2]
    number_of_std += 1

print(total / number_of_std)
conn.close()

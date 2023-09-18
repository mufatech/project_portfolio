import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="mufatech",
    password="mukarram",
    database="myregistration"
)
cursor = connection.cursor()

cursor.execute("SELECT * FROM regpage")
rows = cursor.fetchall()

for row in rows:
    print(row)


cursor.close()
connection.close()

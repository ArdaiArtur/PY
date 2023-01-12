import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  database="proiectweb"

)

mycursor = mydb.cursor()
cursor = mydb.cursor()

mycursor.execute("SELECT * FROM users")
for x in mycursor:
  print(x)

cursor.execute("SELECT usersName FROM users WHERE LENGTH(usersName) > 5 AND usersName IS NOT NULL;")  
for x in cursor:
  print(x)
  
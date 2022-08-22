import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="medaigual"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE x (name VARCHAR(255), address VARCHAR(255))")
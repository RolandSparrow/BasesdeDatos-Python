import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="medaigual"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE hola (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
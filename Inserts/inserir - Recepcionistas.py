import random
import mysql.connector

mydb = mysql.connector.connect(
  host="database-1.ckzqkucrjrxv.us-east-1.rds.amazonaws.com",
  user="admin",
  password="#Pr0jeToD3BaNcoDeD4dos!",
  database="clinicsystem"
)

mycursor = mydb.cursor()


sql = "SELECT id FROM Funcionario WHERE salario = 2000"

mycursor.execute(sql)

resultado = mycursor.fetchall()

for x in resultado:
  for y in x:
    sql = "INSERT INTO Recepcionista (funcionario_id) VALUES (%s)"
    val = (y)
    mycursor.execute(sql, val)

    mydb.commit()


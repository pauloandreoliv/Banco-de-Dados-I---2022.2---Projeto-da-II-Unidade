import random
import mysql.connector

mydb = mysql.connector.connect(
  host="database-1.ckzqkucrjrxv.us-east-1.rds.amazonaws.com",
  user="admin",
  password="#Pr0jeToD3BaNcoDeD4dos!",
  database="clinicsystem"
)

mycursor = mydb.cursor()


sql = "SELECT id FROM Paciente"
mycursor.execute(sql)
pacientes = mycursor.fetchall()
pacientes_ = []
for k in pacientes:
  for y in k:
    pacientes_.append(y)

sql = "SELECT id FROM Consulta"
mycursor.execute(sql)
consultas = mycursor.fetchall()
consultas_ = []
for k in consultas:
  for y in k:
    consultas_.append(y)

sql = "SELECT funcionario_id FROM Recepcionista"
mycursor.execute(sql)
recepcionistas = mycursor.fetchall()
recepcionistas_ = []
for k in recepcionistas:
  for y in k:
    recepcionistas_.append(y)


cont = 0
while cont < len(consultas_):
  consulta = random.choice(consultas_)
  
  paciente = random.choice(pacientes_)
  recepcionista = random.choice(recepcionistas_)

  sql = "SELECT consulta_id FROM Agendamento"
  mycursor.execute(sql)
  agendamentos = mycursor.fetchall()
  agendamentos_ = []
  for k in agendamentos:
    for y in k:
      agendamentos_.append(y)
  if consulta in agendamentos_:
    continue
  else:
    sql = "INSERT INTO Agendamento (consulta_id, paciente_id, recepcionista_funcionario_id) VALUES (%s, %s, %s)"
    val = (consulta, paciente, recepcionista)
    mycursor.execute(sql, val)

    mydb.commit()

    cont+=1

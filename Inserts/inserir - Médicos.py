import random
import mysql.connector

mydb = mysql.connector.connect(
  host="database-1.ckzqkucrjrxv.us-east-1.rds.amazonaws.com",
  user="admin",
  password="#Pr0jeToD3BaNcoDeD4dos!",
  database="clinicsystem"
)

mycursor = mydb.cursor()


especialidades = ["Clínica médica", "Cardiologia", "Dermatologia", "Oftalmologia", "Endocrinologia", "Gastroenterologia", "Geriatria", "Ginecologia", "Infectologia", "Nutrologia", "Oftalmologia", "Oncologia", "Ortopedia", "Otorrinolaringogia", "Pediatria", "Psiquiatria", "Reumatologia", "Urologia", "Neurologia", "Obstetrícia", "Mastologia", "Gastroenterologia", "Angiologia"]
'''especialidade = random.choice(especialidades)

turnos = ["Manhã", "Tarde", "Noite", "Manhã/Tarde", "Tarde/Noite"]
turno = random.choice(turnos)'''



sql = "SELECT id FROM Funcionario WHERE salario = 6000"

mycursor.execute(sql)

resultado = mycursor.fetchall()

for x in resultado:
  for y in x:
    turnos = ["Manhã/Tarde", "Tarde/Noite"]
    turno = random.choice(turnos)
    especialidade = random.choice(especialidades)
    sql = "INSERT INTO Medico (funcionario_id, especialidade, turno) VALUES (%s, %s, %s)"
    val = (y,especialidade,turno)
    mycursor.execute(sql, val)

    mydb.commit()


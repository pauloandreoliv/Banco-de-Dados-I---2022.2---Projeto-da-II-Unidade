import random
import mysql.connector

mydb = mysql.connector.connect(
  host="database-1.ckzqkucrjrxv.us-east-1.rds.amazonaws.com",
  user="admin",
  password="#Pr0jeToD3BaNcoDeD4dos!",
  database="clinicsystem"
)

mycursor = mydb.cursor()


sql = "SELECT paciente_id FROM Prontuario"
mycursor.execute(sql)
resultado = mycursor.fetchall()

for x in resultado:
  for y in x:    
    sql = f"SELECT Consulta.medico_funcionario_id FROM Consulta, Agendamento, Paciente WHERE Consulta.id = Agendamento.consulta_id AND Paciente.id = {y}"
    mycursor.execute(sql)
    result = mycursor.fetchall()

    print(result)
    
    '''for z in result:
      for k in z:
        
    sql = "INSERT INTO Registro (prontuario_id, prontuario_pacinete_id, medico_funcionario_id, observacao, prescricao) VALUES (%s, %s, %s, %s, %s)"
    val = (calcularId(), y)
    mycursor.execute(sql, val)

    mydb.commit()'''


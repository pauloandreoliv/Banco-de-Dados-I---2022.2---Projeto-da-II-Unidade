import random
from datetime import *
import mysql.connector

mydb = mysql.connector.connect(
  host="database-1.ckzqkucrjrxv.us-east-1.rds.amazonaws.com",
  user="admin",
  password="#Pr0jeToD3BaNcoDeD4dos!",
  database="clinicsystem"
)

mycursor = mydb.cursor()


sql = "SELECT funcionario_id FROM Medico"

mycursor.execute(sql)

ids = mycursor.fetchall()

def gerarData():
  dias = list(range(1,31))
  dia = ""
  cont4 = 0
  while cont4<1:
    numero = random.choice(dias)
    dia = '%02d' % numero
    cont4+=1

  meses = list(range(1,13))
  mes = ""
  cont4 = 0
  while cont4<1:
    numero = random.choice(meses)
    mes = '%02d' % numero
    cont4+=1

  anos = list(range(2022,2024))
  ano = ""
  cont4 = 0
  while cont4<1:
    numero = str(random.choice(anos))
    ano = numero
    cont4+=1

  data = ano + "-" + mes + "-" + dia
  return data

for x in ids:
  for y in x:
    sql = f"SELECT turno FROM Medico WHERE funcionario_id = {y}"
    mycursor.execute(sql)
    resultado = mycursor.fetchall()
    for z in resultado:
      for k in z:
        #Horários
        if k == "Manhã":
          horarios = ["10:30","07:15","08:10","09:00","09:30","11:00","12:00","11:50","10:00"]
        if k == "Tarde":
          horarios = ["16:30","17:00","15:10","14:00","12:30","13:00"]
        if k == "Noite":
          horarios = ["18:30","19:00","20:15","20:00","19:30","21:00"]
        if k == "Manhã/Tarde":
          horarios = ["16:00","15:00","16:50","13:30","12:20","14:00","10:00","10:30","11:20","11:15","09:00","09:30","08:30"]
        if k == "Tarde/Noite":
          horarios = ["17:00","16:00","18:50","19:30","15:20","13:40","18:00","14:30","18:20","20:15","22:00","21:30","18:30"]
        horario = random.choice(horarios)

        #Id do médico
        funcionario_medico_id = y

        #Id da consulta
        sql = "SELECT COUNT(id) FROM Consulta"
        mycursor.execute(sql)
        result = mycursor.fetchone()
        id_consulta = result[0] + 1

        #Data
        data = gerarData()
        date = datetime.strptime(data, '%Y-%m-%d').date()

        #Data e horario
        data_horario = data + " " + horario
        horario = datetime.strptime(data_horario, '%Y-%m-%d %H:%M')
        
        #Valor
        valores = [50,100,150,200,300,350,400,450,500]
        valor = random.choice(valores)

        #Estado de pagamento
        estados = ["Pendente", "Pagamento efetuado"]
        estado = random.choice(estados)

        #Insert
        sql = "INSERT INTO Consulta (id, medico_funcionario_id, data, horario, observacao, valor, estado_de_pagamento) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (id_consulta, funcionario_medico_id, date, horario, "Nenhuma", valor, estado)
        mycursor.execute(sql, val)

        mydb.commit()

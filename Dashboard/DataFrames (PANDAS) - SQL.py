import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
  host="database-1.ckzqkucrjrxv.us-east-1.rds.amazonaws.com",
  user="admin",
  password="#Pr0jeToD3BaNcoDeD4dos!",
  database="clinicsystem"
)

mycursor = mydb.cursor()

# Retorna as especialidades sem repetiçôes
sql = "SELECT DISTINCT especialidade FROM Medico ORDER BY especialidade DESC"
mycursor.execute(sql)
especialidade = mycursor.fetchall()
especialidade_list = []
for k in especialidade:
  for y in k:
    especialidade_list.append(y)

# Retorna a quantidade de consultas por especialidade
resquest_qtd = "SELECT COUNT(Medico.especialidade) FROM Medico, Consulta WHERE Consulta.medico_funcionario_id = Medico.funcionario_id GROUP BY Medico.especialidade ORDER BY especialidade DESC"
mycursor.execute(resquest_qtd)
quantidade = mycursor.fetchall()
quantidade_list = []

for i in quantidade:
    for item in i:
        quantidade_list.append(item)
#Grafico 1
df_agendxEsp = pd.DataFrame({
    "Especialidades": especialidade_list,
    "Quantidade": quantidade_list
})

print("####\nConsultas por especialidade:")
print(df_agendxEsp)
print("")



#########################################


# Realizando a consulta por mes
resultados_consultas_mes = []

for k in list(range(1,13)):
    num = f"{k:02}"
    sql = f"SELECT COUNT(id) FROM Consulta WHERE data LIKE '%%%%-{num}-%%'"
    mycursor.execute(sql)
    resultado = mycursor.fetchall()
    mes = resultado[0]
    resultados_consultas_mes.append(mes)


resultados_consultas_mes = list(reversed(resultados_consultas_mes))

# retorna uma lista com os números de consulta por mês
resultados_consultas_mes_2 = []
for k in resultados_consultas_mes:
    for y in k:
        resultados_consultas_mes_2.append(y)

df_evolucao_mensal = pd.DataFrame({
    "Quantidade": resultados_consultas_mes_2,
    "Mes": ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
})

print("####\nConsultas por mês:")
print(df_evolucao_mensal)
print("")



#########################################

# Retorna a quantidade de agendamento por tipo sanguineo
sql = "SELECT COUNT(Pa.tipo_sanguineo) FROM Agendamento as Ag, Paciente as Pa WHERE Ag.paciente_id = Pa.id GROUP BY Pa.tipo_sanguineo ORDER BY Pa.tipo_sanguineo"
mycursor.execute(sql)
tipo_sanguineo = mycursor.fetchall()
qtd_tipo_sanguineo_list = []
for k in tipo_sanguineo:
  for y in k:
    qtd_tipo_sanguineo_list.append(y)

# Retorna uma lista com os tipos sanguíneos da base de dados
sql = "SELECT DISTINCT tipo_sanguineo FROM Paciente ORDER BY tipo_sanguineo"
mycursor.execute(sql)
tipo_sanguineo = mycursor.fetchall()
tipo_sanguineo_list = []
for k in tipo_sanguineo:
  for y in k:
    tipo_sanguineo_list.append(y)


#Grafico 3
df_agendamento_sanguineo = pd.DataFrame({
    "Quantidade": qtd_tipo_sanguineo_list,
    "Tipo Sanguíneo": tipo_sanguineo_list
})

print("####\nConsultas por tipo sanguíneo")
print(df_agendamento_sanguineo)
print("")



#########################################

# Retorna a média do valor da consulta por especialidade
media = "SELECT AVG(C.valor)  FROM Medico as M, Consulta as C WHERE C.medico_funcionario_id = M.funcionario_id GROUP BY M.especialidade ORDER BY M.especialidade"
mycursor.execute(media)
media_esp = mycursor.fetchall()
media_list = []

for i in media_esp:
    for item in i:
        media_list.append(item)

#Grafico 4
especialidade_result = list(reversed(especialidade_list))
df_consultaxEsp = pd.DataFrame({
    "Especialidades": especialidade_result,
    
    "(R$) Valor": media_list
})

print("####\nMédia do valor da consulta por especialidade")
print(df_consultaxEsp)
print("")



#########################################

# Retorna a quantidade total de médicos e Recepcionistas
sql = f"SELECT COUNT(Medico.funcionario_id), ((SELECT COUNT(id) FROM Funcionario) - COUNT(Medico.funcionario_id)) FROM Funcionario, Medico WHERE Funcionario.id = Medico.funcionario_id"
mycursor.execute(sql)
medicos_recepcionistas = mycursor.fetchall()

medicos_recepcionistas_list = []
for k in medicos_recepcionistas:
    for y in k:
        medicos_recepcionistas_list.append(y)
        
#Grafico 5

df_medicoxRecep = pd.DataFrame({
    "Função": ["Médico", "Recepcionista"],
    
    "Qtd": medicos_recepcionistas_list

})

print("####\nQuantidade de Médicos vs Quantidade de Recepcionistas")
print(df_medicoxRecep)
print("")



#########################################

# Retorna a quantidade de funcinários pela ordem crescente da faixa salarial

sql = "SELECT COUNT(id) FROM Funcionario GROUP BY salario ORDER BY salario ASC"
mycursor.execute(sql)
funcionario = mycursor.fetchall()

funcionario_list = []
for k in funcionario:
    for y in k:
        funcionario_list.append(y) 


# Retorna as Faixas salariais do funcionario pela ordem crescente
sql = "SELECT DISTINCT salario FROM Funcionario ORDER BY salario ASC"
mycursor.execute(sql)
funcionario_salario = mycursor.fetchall()

funcionario_salario_list = []
for k in funcionario_salario:
    for y in k:
        funcionario_salario_list.append(y) 

#Grafico 6

df_qtdFuncionxSalario = pd.DataFrame({

    "(Qtd) Fucinonários" : funcionario_list,
    "Faixa Salarial" : funcionario_salario_list
    

})

print("####\nQuantidade de funcinários pela ordem crescente da faixa salarial")
print(df_qtdFuncionxSalario)
print("")

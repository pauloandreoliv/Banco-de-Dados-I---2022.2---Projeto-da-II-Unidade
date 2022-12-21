import random
import mysql.connector

mydb = mysql.connector.connect(
  host="database-1.ckzqkucrjrxv.us-east-1.rds.amazonaws.com",
  user="admin",
  password="#Pr0jeToD3BaNcoDeD4dos!",
  database="clinicsystem"
)

mycursor = mydb.cursor()

sql = "INSERT INTO  (id, nome, email, telefone, salario) VALUES (%s, %s, %s, %s, %s)"
val = []


cont = 11
while cont <= 100:
    principal = ["MARIA", "ANA", "PEDRO", "AUGUSTO", "CLÁUDIO", "PAULO", "PEDRO", "ADRIANA", "ROBERTO", "LUIZ", "JOSÉ", "JOÃO", "VITÓRIA", "ROBERTA", "CLÁUDIA", "MARCOS", "PIETRA", "LUÍSA", "CLARA", "JOANA"]
    sobrenome = ["SILVA", "COSTA", "SÁ", "MELO", "LIMA", "GONÇALVES", "CORREIA", "GONZAGA", "BRAGANÇA", "SOUZA", "OLIVEIRA", "ALBUQUERQUE", "PEREIRA"]
    nome = random.choice(principal) + " " + random.choice(sobrenome)

    numeros = list(range(0,11))
    numero = random.choice(numeros)
    email = nome[0] + nome[1] + f"{numero}" + "@gmail.com"

    
    telefone = "819"
    cont2 = 0
    while cont2<9:
        numero = str(random.choice(numeros))
        telefone +=numero
        cont2+=1

    salarios = [1200, 2000, 4000, 6000]
    salario = random.choice(salarios)
    
    dados = (cont, nome, email, telefone, salario)
    val.append(dados)
    cont+=1

mycursor.executemany(sql, val)

mydb.commit()

print(val)

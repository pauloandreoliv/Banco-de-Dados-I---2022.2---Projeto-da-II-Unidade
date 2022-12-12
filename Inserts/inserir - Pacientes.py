import random
import mysql.connector

mydb = mysql.connector.connect(
  host="database-1.ckzqkucrjrxv.us-east-1.rds.amazonaws.com",
  user="admin",
  password="#Pr0jeToD3BaNcoDeD4dos!",
  database="clinicsystem"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Paciente (id,  cpf, nome, endereco, email, telefone, data_nascimento, tipo_sanguineo, alergia, observacao, responsavel) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = []


cont = 1
while cont <= 200:
    #NOME
    principal = ["MARIA", "ANA", "PEDRO", "AUGUSTO", "CLÁUDIO", "PAULO", "PEDRO", "ADRIANA", "ROBERTO", "LUIZ", "JOSÉ", "JOÃO", "VITÓRIA", "ROBERTA", "CLÁUDIA", "MARCOS", "PIETRA", "LUÍSA", "CLARA", "JOANA", "DIANA", "ARTUR", "ARTHUR", "MARCELO", "ALDERI", "CAIO", "CARLA", "BRUNA", "BRUNO", "BRENO", "BRENDA", "LUANA", "LAURA", "MATEUS", "MATIAS", "OTÁVIO", "ALANA", "RAÍSSA", "KETLEN", "KARINE", "CAROLINA", "HEITOR", "RUAN", "FELIPE", "FILIPE", "FELIPA", "TÂNIA", "BETÂNIA", "DIEGO", "MOISÉS", "DIOGO", "GABRIEL"]
    sobrenome = ["SILVA", "COSTA", "SÁ", "MELO", "LIMA", "GONÇALVES", "CORREIA", "GONZAGA", "BRAGANÇA", "BEZERRA", "SOUZA", "OLIVEIRA", "DE OLIVEIRA FEITOSA", "ALBUQUERQUE", "PEREIRA", "CARVALHO", "GOMES", "ROCHA", "DIAS", "GOUVEIA", "UCHÔA", "PEIXOTO", "FIGUEIRA", "MACHADO", "ASSIS", "BRITO", "BARBOSA", "PEIXOTO DA SILVA", "OLIVEIRA DA SILVA", "DA SILVA OLIVEIRA", "CORREIA MENDONÇA", "NETTO", "MOURA", "SOUZA MORAES", "DA LIMA VASCONCELOS", "PORTELLA", "VASCONCELOS", "FRANCISCO", "CAMARGO", "BORBA", "DA SILVA BORBA", "MARCONDES", "XAVIER"]
    nome = random.choice(principal) + " " + random.choice(sobrenome)

    #E-MAIL
    numeros = list(range(0,11))
    numero = random.choice(numeros)
    tipos_email = ["@hotmail.com", "@outlook.com", "@yahooo.com", "@gmail.com"]
    tipo_email = random.choice(tipos_email)
    email = nome[0] + nome[1] + f"{numero}" + tipo_email

    #TELEFONE
    telefone = "819"
    cont2 = 0
    while cont2<9:
        numero = str(random.choice(numeros))
        telefone +=numero
        cont2+=1
    #CPF
    cpf = ""
    cont3 = 0
    while cont3<11:
        numero = str(random.choice(numeros))
        cpf +=numero
        cont3+=1

    #ENDEREÇO
    numero_endereco = list(range(1,3000))
    numero = str(random.choice(numero_endereco))
    tipos = ["Avenida", "Rua"]
    tipo = random.choice(tipos)
    ruas = ["Marechal", "Bacalhau", "Um", "Dois", "Presidente", "Maestro", "Professor", "Procurador", "Governador", "Cantor Luiz Gonzaga", "Rio Branco", "Dr. José", "Bem-te-vi", "Beija-flor", "Girassol", "Margarida", "Encruzilhada", "Nossa Senhora", "Paulista", "Olinda", "Recife", "Japão", "Portugal", "Espanha", "Borborema", "São Paulo", "João XX", "Argentina", "Marrocos", "Croácia"]
    rua = random.choice(ruas)
    bairros = ["Jardins", "Rio", "Alto", "Engenho", "Leblon", "Praia", "Porto", "Maré", "Mar", "Recanto", "Vila", "Itamaracá", "Brejo", "Janga", "Paulista", "Recife", "Centro", "Orla", "Mata", "Reserva", "Parque", "Caminho", "Abraço", "Cidade Universitária", "Várzea", "Casa Caiada", "Água Fria", "Rio Doce", "Sé", "Aurora", "Santo Amaro"]
    bairro = random.choice(bairros)
    cidades = ['Olinda','Paulista','Vicencia', 'Agua Preta', 'Agua Bela', 'Arcoverde','Belo Jardim', "Belém de Maria", 'Bonito','Condado','Ilha de Itamaraca','Jaboatão Dos Guararapes  ', 'Jaqueira', 'Joaquim Nabuco  ', 'Limoeiro', 'Recife','Machados','Nazaré da Mata','Palmares','Pesqueira','Petrolina', 'Escada', 'Chã de Alegria','Carnaíba Afogados da Ingazeira','Abreu e Lima','Igarassu', 'Santa Cruz', 'São José do Egito', 'Ribeirão']
    cidade = random.choice(cidades)
    endereco = tipo + " " + rua + ", " + numero + ", " + bairro + ", " + cidade + ", Pernambuco"

    #DATA DE NASCIMENTO
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

    anos = list(range(1969,2022))
    ano = ""
    cont4 = 0
    while cont4<1:
        numero = str(random.choice(anos))
        ano = numero
        cont4+=1

    data_nascimento = dia + "-" + mes + "-" + ano

    #TIPO SANGUÍNEO
    tipos_sanguineos = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    tipo_sanguineo = random.choice(tipos_sanguineos)

    #ALERGIA
    alergias = ["Nenhuma", "Nenhuma", "Nenhuma", "Nenhuma", "Nenhuma", "Nenhuma", "Nenhuma", "Nenhuma", "Nenhuma", "Aspirina", "Cefalexina", "Amendoim", "Soja", "Leite", "Chocolate", "Camarão", "Corticóides", "Benzoato", "Perfumes e remédios com corante", "Tylenol e dipirona", "Passiflora", "Clonazepam", "Neolefrin", "Tadalafila e Pantoprazol", "Artovastina", "Esomeprazol", "Seki prazol", "Omeprazol", "Lipanon", "Antibióticos", "Tylenol", "Advil", "Ibuprofeno", "Corante", "Paracetamol", "Dipirona", "Antibióticos sulfonamida", "Penicilina", "Corante de raios X", "Anestésicos", "Neomicina", "Dicoflenaco", "Naproxeno", "Carbamazepina", "Lamotrigina", "Morfina", "Fenitoína", "Nimesulida"]
    alergia = random.choice(alergias)

    #OBSERVAÇÃO
    observacoes = ["Nenhuma", "Nenhuma", "Nenhuma", "Nenhuma", "Necessita de acompanhante", "Paciente prioritário"]
    observacao = random.choice(observacoes)

    #RESPONSÁVEL
    sim_nao = [0,1,0]
    escolha = random.choice(sim_nao)
    if escolha == 0:
        responsavel = "Nenhum"
    else:
        responsavel = random.choice(principal) + " " + random.choice(sobrenome)
    
    dados = (cont, cpf, nome, endereco, email, telefone, data_nascimento, tipo_sanguineo, alergia, observacao, responsavel)
    val.append(dados)
    cont+=1
    

mycursor.executemany(sql, val)

mydb.commit()

print(val)

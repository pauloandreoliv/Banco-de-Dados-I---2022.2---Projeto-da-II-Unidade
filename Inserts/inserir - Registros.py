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
    sql = f"SELECT consulta_id FROM Agendamento WHERE paciente_id = {y}"
    mycursor.execute(sql)
    resultado2 = mycursor.fetchall()

    for da_consulta in resultado2:
      for id_da_consulta in da_consulta:
        sql = f"SELECT medico_funcionario_id FROM Consulta WHERE id = {id_da_consulta}"
        mycursor.execute(sql)
        resultado3 = mycursor.fetchall()

        observacoes = ["Paciente com sintomas gripais", "Paciente com queixa de dores constantes na cabeça", "Paciente iniciando tratamento com antibióticos", "NENHUMA OBSERVAÇÃO", "NENHUMA OBSERVAÇÃO", "NENHUMA OBSERVAÇÃO", "NENHUMA OBSERVAÇÃO", "NENHUMA OBSERVAÇÃO", "Paciente com deficiência de vitaminas", "Paciente com redução da pressão arterial", "Paciente com incômodo intestinal", "Paciente com infecção fúngica", "Paciente com infecção bacteriana", "Paciente com infecção bacteriana não identificada", "Paciente com dores musculares constantes", "Paciente imunodeprimido", "COVID-19", "H3N2", "ZIKA VÍRUS", "DENGUE", "FEBRE AMARELA", "FEBRE", "HIPOGLICEMIA", "AUMENTO DO RITMO CARDÍACO", "DOR NA PANTURRILHA ESQUERDA", "PACIENTE COM QUADRO DE FATURA NO ANTEBRAÇO", "PACIENTE COM DERMATITE", "PACIENTE DIAGNOSTICADO COM TUMOR BENIGNO", "PACIENTE DIAGNOSTICADO COM HEPATITE A", "PACIENTE DIAGNOSTICADO COM MININGITE", "PACIENTE COM QUEDA DE HEMÁCIAS", "PACIENTE SAUDÁVEL. TAXAS DENTRO DOS NÍVEIS NORMAIS", "PACIENTE AFIRMA REALIZAR O USO DE MEDICAMENTOS CONTROLADOS", "PACIENTE SAUDÁVEL", "PACIENTE COM INCHAÇO NA REGIÃO DO FÍGADO", "PACIENTE SEM SINAIS DE COMORBIDADES", "PACIENTE COM TAXAS DENTRO DO ACEITÁVEL", "PACIENTE EM TRATAMENTO", "PACIENTE COM QUADRO DE ANSIEDADE GRAVE"]
        observacao = random.choice(observacoes)

        prescricoes = ["Dipirona 10mg", "Ibuprofeno de 8 em 8h", "Paracetamol a cada 8h ou em caso de dor forte", "Repouso e uso de passiflora", "Ingestão de alimentos sem corantes artificiais", "Não realizar esforço físico até a cicatrização e retirada dos pontos", "Trocar o curativo de forma periódica", "Receita de Rivotril", "Receita de Cefalexina", "Recomendação da relização de exames de sangue de rotina", "Ingestão de 2,5L mínimos de água diariamente", "Ingestão de frutas ricas em fibras", "Alimentação rica em vitamina K", "Evitar alimentos gordurosos", "Afastamento de atividades laborais por 5 dias", "Realização de teste de COVID-19", "Afastamento de atividades laborais por 3 dias", "Uso de Enterogermina. Seguir rotina proposta na bula do medicamento", "Ingestão de comprimidos de colecalciferol 15.000 UI a cada 7 dias por 3 meses", "Repouso absoluto e ingestão de alimentos pastosos", "Ingestão de alimentos pastosos", "Multigripe, nimesulida, soro fisiológico", "Soro fisiológico", "Colírio lubrificante de 8 em 8 h", "Colonoscopia", "Ultrassom da córnea", "Ultrassom da panturrilha direta", "Ultrassom da região do estômago", "Ultrassom da tireóide", "Raio-x da perna esquerda", "Raio-x da perna direita", "Raio-x facial", "Raio-x completo", "Tumografia", "Sem prescrições", "Sem prescrições", "Sem prescrições", "Sem prescrições"]
        prescricao = random.choice(prescricoes)


        sql = "SELECT prontuario_paciente_id, medico_funcionario_id FROM Registro"
        mycursor.execute(sql)
        para_verificar = mycursor.fetchall()

        for k in para_verificar:
          if k == (y, resultado3[0][0]):
            break
          else:
            sql = "INSERT IGNORE INTO Registro (prontuario_paciente_id, medico_funcionario_id, observacao, prescricao) VALUES (%s, %s, %s, %s)"
            val = (y, resultado3[0][0], observacao, prescricao)

            mycursor.execute(sql, val)

            mydb.commit()

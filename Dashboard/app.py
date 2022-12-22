

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


app = dash.Dash(external_stylesheets=[dbc.themes.MORPH])


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

# Retorna a quantidade de consulta por especialidade
resquest_qtd = "SELECT COUNT(Medico.especialidade) FROM Medico, Consulta WHERE Consulta.medico_funcionario_id = Medico.funcionario_id GROUP BY Medico.especialidade ORDER BY especialidade DESC"
mycursor.execute(resquest_qtd)
quantidade = mycursor.fetchall()
quantidade_list = []

for i in quantidade:
    for item in i:
        quantidade_list.append(item)



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





# Retorna a média do valor da consulta por especialidade
media = "SELECT AVG(C.valor)  FROM Medico as M, Consulta as C WHERE C.medico_funcionario_id = M.funcionario_id GROUP BY M.especialidade ORDER BY M.especialidade"
mycursor.execute(media)
media_esp = mycursor.fetchall()
media_list = []

for i in media_esp:
    for item in i:
        media_list.append(item)



# Retorna a quantidade total de médicos e Recepcionistas
sql = f"SELECT COUNT(Medico.funcionario_id), ((SELECT COUNT(id) FROM Funcionario) - COUNT(Medico.funcionario_id)) FROM Funcionario, Medico WHERE Funcionario.id = Medico.funcionario_id"
mycursor.execute(sql)
medicos_recepcionistas = mycursor.fetchall()

medicos_recepcionistas_list = []
for k in medicos_recepcionistas:
    for y in k:
        medicos_recepcionistas_list.append(y) 



# Retorna a quantidade de funcinário pela ordem crescente da faixa salarial

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

colors = {
    'background': '#97d4d6',
    'text': '#022933'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options



#Grafico 1
df_agendxEsp = pd.DataFrame({
    "Especialidades": especialidade_list,
    "Quantidade": quantidade_list
})


fig_bar_h = px.bar(df_agendxEsp, title="Consultas por Especialidades", x="Quantidade", y="Especialidades",
 barmode="group", orientation="h", color_discrete_sequence=["#022933"])

fig_bar_h.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']    
    
)

#Grafico 2
df_evolucao_mensal = pd.DataFrame({
    "Quantidade": resultados_consultas_mes_2,
    "Mes": ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
})

fig_line = px.line(df_evolucao_mensal, title="Evolução Mensal de Consultas", x="Mes", y="Quantidade", 
markers="True", color_discrete_sequence=["#022933"])

#Grafico 3
df_agendamento_sanguineo = pd.DataFrame({
    "Quantidade": qtd_tipo_sanguineo_list,
    "Tipo Sanguíneo": tipo_sanguineo_list
})

fig_bar_2 = px.bar(df_agendamento_sanguineo, title="Agendamento por Tipo Sanguíneo", x="Tipo Sanguíneo", y="Quantidade", 
barmode="group", color_discrete_sequence=["#022933"])


#Grafico 4
especialidade_result = list(reversed(especialidade_list))
df_consultaxEsp = pd.DataFrame({
    "Especialidades": especialidade_result,
    
    "(R$) Valor": media_list
})

fig_bar = px.bar(df_consultaxEsp, title="Média do valor das consultas", x="Especialidades", y="(R$) Valor",
 barmode="group", color_discrete_sequence=["#022933"])

fig_bar.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'] ) 


#Grafico 5

df_medicoxRecep = pd.DataFrame({
    "Função": ["Médico", "Recepcionista"],
    
    "Qtd": medicos_recepcionistas_list

})
fig_piz = px.pie(df_medicoxRecep, values='Qtd', names='Função',
             title='Total (Qtd) Médico X Recepcionista', color_discrete_sequence=["#022933", "#97d4d6"])
            #  hover_data=['lifeExp'], labels={'lifeExp':'life expectancy'})
fig_piz.update_traces(textposition='inside', textinfo='percent+label')


#Grafico 6

df_qtdFuncionxSalario = pd.DataFrame({

    "(Qtd) Fucinonários" : funcionario_list,
    "Faixa Salarial" : funcionario_salario_list
    

})
fig_histo = px.histogram(df_qtdFuncionxSalario, title="(Qtd) Funcionários X Faixa Salarial", x="Faixa Salarial", y="(Qtd) Fucinonários", nbins=8, color_discrete_sequence=["#022933"])

app.layout = html.Div( children=[
    html.H1(
        children='Clinic System',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(className='h2-t',
    children=[
    html.H2('Gerenciamento Clínico', className='h2')]
),


    dcc.Graph(
        id='fig_bar_h',
        figure=fig_bar_h
    ),

    html.Div(children=[
        dcc.Graph(
        id='fig_bar',
        figure=fig_line,
        style={'width': 800, 'padding': 10}),

        dcc.Graph(
        id='fig_lin2_2',
        figure=fig_bar_2,
        style={'width': 800, 'padding': 10}),


    ], style={'display': 'flex', 'flex-direction': 'row'}),

      dcc.Graph(
        id='fig_bar',
        figure=fig_bar
    ),

     dcc.Graph(
        id='fig_piz',
        figure=fig_piz
    ),

      dcc.Graph(
        id='fig_histo',
        figure=fig_histo
    ),


    dbc.Container(
    dbc.Alert("Debug OK", color="success"),
    className="p-5")
])

if __name__ == '__main__':
    app.run_server(debug=True)

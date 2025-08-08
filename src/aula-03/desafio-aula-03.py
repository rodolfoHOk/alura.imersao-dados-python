import pandas as pd
import plotly.express as px

data_url = 'https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv'

df = pd.read_csv(data_url)

renomear_colunas = {
  'work_year': 'ano',
  'experience_level': 'senioridade',
  'employment_type': 'contrato',
  'job_title': 'cargo',
  'salary': 'salario',
  'salary_currency': 'moeda',
  'salary_in_usd': 'usd',
  'employee_residence': 'residencia',
  'remote_ratio': 'remoto',
  'company_location': 'empresa',
  'company_size': 'tamanho_empresa'
}
df.rename(columns=renomear_colunas, inplace=True)

senioridade = {
  'SE': 'senior',
  'MI': 'pleno',
  'EN': 'junior',
  'EX': 'executivo'
}
df['senioridade'] = df['senioridade'].replace(senioridade)

contrato = {
  'FT': 'integral',
  'PT': 'parcial',
  'CT': 'contrato',
  'FL': 'freelancer'
}
df['contrato'] = df['contrato'].replace(contrato)

tamanho_empresa = {
  'L': 'grande',
  'S': 'pequena',
  'M':	'media'
}
df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)

mapa_trabalho = {
    0: 'presencial',
    100: 'remoto',
    50: 'hibrido'
}
df['remoto'] = df['remoto'].replace(mapa_trabalho)

df_limpo = df.dropna()

df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype('int64'))

cientista_dados = 'Data Scientist'
df_cientista_dados = df_limpo[df_limpo['cargo'] == cientista_dados]

# print(df_cientista_dados.head())

media_salario_cientista_dados_por_pais = df_cientista_dados.groupby('residencia')['usd'].mean()

# print(media_salario_cientista_dados_por_pais)

media_salario_cientista_dados_por_pais_ordem = media_salario_cientista_dados_por_pais.sort_values(ascending=True)

fig = px.bar(media_salario_cientista_dados_por_pais_ordem.reset_index(),
             x='usd',
             y='residencia',
             orientation='h',
             title='Média salarial de Cientista de dados por país (USD)',
             labels={'residencia': 'País', 'usd': 'Salário Médio (USD)'})
fig.show()

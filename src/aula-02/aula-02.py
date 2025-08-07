import pandas as pd
import numpy as np

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

# print(df.head())
# print(df.isnull())
# print(df.isnull().sum())
# print(df['ano'].unique())
# print(df[df.isnull().any(axis=1)])

df_salarios = pd.DataFrame({
  'nome': ['Ana', 'Bruno', 'Carlos', 'Daniele', 'Eduardo', 'Val'],
  'salario': [4000, np.nan, 3500, np.nan, 5000, 100000]
})

df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))
df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median().round(2))

# print(df_salarios)

df_temperaturas = pd.DataFrame({
    'dia': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'],
    'temperatura': [30, np.nan, np.nan, 28, 27]
})

df_temperaturas['preenchido_ffill'] = df_temperaturas['temperatura'].ffill()
df_temperaturas['preenchido_bfill'] = df_temperaturas['temperatura'].bfill()

# print(df_temperaturas)

df_cidades = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', 'Daniele', 'Eduardo'],
    'cidade': ['São Paulo', np.nan, 'Curitiba', np.nan, 'Belém']
})

df_cidades['cidade_preenchida'] = df_cidades['cidade'].fillna('Não informado')

# print(df_cidades)

df_limpo = df.dropna()

# print(df_limpo.isnull().sum())
# print(df_limpo.head())
# print(df_limpo.info())

df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype('int64'))

# print(df_limpo.head())
# print(df_limpo.info())

# PRINT

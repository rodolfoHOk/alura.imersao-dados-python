import pandas as pd

data_url = 'https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv'

df = pd.read_csv(data_url)

# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.shape)

# rows, columns = df.shape[0], df.shape[1]
# print("linhas:", rows)
# print("colunas:", columns)

# print(df.columns)

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

# print(df.head())

# print(df['senioridade'].value_counts())
## SE, MI, EN, EX (senior, pleno, junior, executivo/liderança)
# print(df['contrato'].value_counts())
## FT, CT, PT, FL (full-time, contract-temporary, partial-time, free-lance)
# print(df['remoto'].value_counts())
# print(df['tamanho_empresa'].value_counts())
## M, L, S (medium, large, small)

senioridade = {
  'SE': 'senior',
  'MI': 'pleno',
  'EN': 'junior',
  'EX': 'executivo'
}
df['senioridade'] = df['senioridade'].replace(senioridade)

# print(df['senioridade'].value_counts())

contrato = {
  'FT': 'integral',
  'PT': 'parcial',
  'CT': 'contrato',
  'FL': 'freelancer'
}
df['contrato'] = df['contrato'].replace(contrato)

# print(df['contrato'].value_counts())

tamanho_empresa = {
  'L': 'grande',
  'S': 'pequena',
  'M':	'media'
}
df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)

# print(df['tamanho_empresa'].value_counts())

mapa_trabalho = {
    0: 'presencial',
    100: 'remoto',
    50: 'hibrido'
}
df['remoto'] = df['remoto'].replace(mapa_trabalho)

# print(df['remoto'].value_counts())
# print(df.head())

# print(df.describe(include="object"))
# print(df.describe())

# PANDAS

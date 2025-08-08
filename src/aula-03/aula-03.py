import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

# print(df_limpo.head())

plt.figure(figsize=(8,5))
df_limpo['senioridade'].value_counts().plot(kind='bar', title='Distribuição de senioridade')
plt.xticks(rotation=45, ha='right')
plt.xlabel("Senioridade")
plt.ylabel("Quantidade de pessoas")
plt.tight_layout()
plt.savefig("src/aula-03/grafico-01.png")

# plt.figure(figsize=(8,5))
# sns.barplot(data=df_limpo, x='senioridade', y='usd')
# plt.title("Salário médio por senioridade")
# plt.xlabel("Senioridade")
# plt.ylabel("Salário médio anual (USD)")
# plt.savefig("src/aula-03/grafico-02.png")

ordem = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=True).index
# print(ordem)
plt.figure(figsize=(8,5))
sns.barplot(data=df_limpo, x='senioridade', y='usd', order=ordem)
plt.title("Salário médio por senioridade")
plt.xlabel("Senioridade")
plt.ylabel("Salário médio anual (USD)")
plt.savefig("src/aula-03/grafico-02.png")

plt.figure(figsize=(10,5))
sns.histplot(df_limpo['usd'], bins=50, kde=True)
plt.title("Distribuição dos salários anuais")
plt.xlabel("Salário em USD")
plt.ylabel("Frequência")
plt.savefig("src/aula-03/grafico-03.png")

plt.figure(figsize=(8,5))
sns.boxplot(x=df_limpo['usd'])
plt.title("Boxplot Salário")
plt.xlabel("Salário em USD")
plt.savefig("src/aula-03/grafico-04.png")

# ordem_senioridade = ['junior', 'pleno', 'senior', 'executivo']
# plt.figure(figsize=(8,5))
# sns.boxplot(x='senioridade', y='usd', data=df_limpo, order=ordem_senioridade)
# plt.title("Boxplot da distribuição por senioridade")
# plt.ylabel("Senioridade")
# plt.ylabel("Salário em USD")
# plt.savefig("src/aula-03/grafico-05.png")

ordem_senioridade = ['junior', 'pleno', 'senior', 'executivo']
plt.figure(figsize=(8,5))
sns.boxplot(x='senioridade', y='usd', data=df_limpo, order=ordem_senioridade, palette='Set2', hue='senioridade')
plt.title("Boxplot da distribuição por senioridade")
plt.ylabel("Senioridade")
plt.ylabel("Salário em USD")
plt.savefig("src/aula-03/grafico-05.png")

senioridade_media_salario = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).reset_index()
fig = px.bar(senioridade_media_salario,
             x='senioridade',
             y='usd',
             title='Média Salarial por Senioridade',
             labels={'senioridade': 'Nível de Senioridade', 'usd': 'Média Salarial Anual (USD)'})
fig.show()

# remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
# remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
# fig2 = px.pie(remoto_contagem,
#               names='tipo_trabalho',
#               values='quantidade',
#               title='Proporção dos tipos de trabalho')
# fig2.show()

remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
fig2 = px.pie(remoto_contagem,
              names='tipo_trabalho',
              values='quantidade',
              title='Proporção dos tipos de trabalho',
              hole=0.5)
fig2.update_traces(textinfo='percent+label')
fig2.show()

# MATPLOTLIB

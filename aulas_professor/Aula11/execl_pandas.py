import pandas as pd
# Leitura de arquivo Excel
# df = pd.read_excel('dados.xlsx', sheet_name='Vendas')
df = pd.read_csv('dados.csv', sep=';')
# Análise básica
print(df.head())
print(df.describe())
# Filtragem de dados
idade_maior = df[df['idade'] >= 30]
# Escrita em novo arquivo
idade_maior.to_excel('idade_maior.xlsx', index=False)
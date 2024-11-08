import os

os.system('cls')

import pandas as pd 


from sqlalchemy import create_engine


import numpy as np



host = 'localhost'
user = 'root'
password = 'root'
database = 'bd_loja'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# Leitura dos dados da tabela de produtos
df_estoque = pd.read_sql('tb_produtos', engine)
# print(df_estoque)

# # Calcula o valor do estoque por linha
df_estoque['TotalEstoque'] = (df_estoque['QuantidadeEstoque'] * df_estoque['Valor'])
# print(df_estoque[['NomeProduto','TotalEstoque']])

df_agrupado = df_estoque.groupby('NomeProduto').agg({
    'QuantidadeEstoque' : 'sum',
    'TotalEstoque' : 'sum'
}).reset_index()

print(df_agrupado)

df_ordenado = df_agrupado.sort_values(by='TotalEstoque', ascending=False)
print(df_ordenado[['NomeProduto', 'TotalEstoque']])

print(f'\nTotal geral em estoque: R${df_ordenado["TotalEstoque"].sum()}')


array_total_estoque = np.array(df_estoque['TotalEstoque'])

media = np.mean(array_total_estoque)
mediana = np.median(array_total_estoque)

print(f'\n{media}')
print(mediana)

distancia = (media - mediana)/mediana
print(distancia)

distancia_media_mediana = abs((media - mediana) / mediana)
print(f'\nMédia do valor total: R${media: .2f}')
print(f'Mediana do valor total: R${mediana: .2f}')
print(f'Distância entre média e mediana: {distancia_media_mediana: .2f}')


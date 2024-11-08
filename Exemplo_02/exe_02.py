import os

os.system('cls')

import pandas as pd 


from sqlalchemy import create_engine


import numpy as np



#Obter dados
try:
    print('Obtendo dados...')
    ENDEREÇO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    # Encodings: utf-8, iso8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDEREÇO_DADOS, sep=';', encoding='iso-8859-1')

    # Delimitando somente as variáveis do Exemplo01: munic e roubo_veiculo
    df_roubo_veiculo = df_ocorrencias[['munic', 'roubo_veiculo']]

    df_roubo_veiculo = df_roubo_veiculo.groupby(['munic']).sum(['Roubo_veiculo']).reset_index()

    print(df_roubo_veiculo.head())
    print('\nDados obtidos com sucesso!')

    

except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()



# Gerando informações...
try: 
    print('\nCalculando informações sobre padrão de roubo de veículos...')

    # Array Numpy
    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])

    # Média de roubo_veículo
    media_roubo_veiculo = np.mean(array_roubo_veiculo)

    # Mediana de roubo_veiculo - Divide a distribuição em duas partes iguais
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)

    
    distancia = abs((media_roubo_veiculo - mediana_roubo_veiculo)/mediana_roubo_veiculo *100)

    print(f'Média de roubo de veiculo: {media_roubo_veiculo}')
    print(f'Mediana de roubo de veiculo: {mediana_roubo_veiculo}')
    print(f'Diferença entre média e mediana {distancia: .2f}%')

except Exception as e:
    print(f'Erro ao obter informações sobre padrão de roubo de veículos: {e}')
    exit()
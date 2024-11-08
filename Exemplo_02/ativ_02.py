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

    # Delimitando somente as variáveis do Exemplo01: munic e estelionato
    df_estelionato = df_ocorrencias[['munic', 'estelionato']]

    df_t_estelionato = df_estelionato.groupby(['munic']).sum(['estelionato']).reset_index()

    df_estelionato1 = df_estelionato.groupby(['estelionato'])

    print(df_estelionato.head())
    print(f'Total de Estelionato: {df_t_estelionato}')
    print('\nDados obtidos com sucesso!')

    

except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()



# Gerando informações...
try: 
    print('\nCalculando informações sobre estelionato...')

    array_total_estelionato = np.sum(df_estelionato1)
    print(f'total {array_total_estelionato}')

    # Array Numpy
    array_estelionato = np.array(df_estelionato['estelionato'])

    # Média de roubo_veículo
    media_estelionato = np.mean(array_estelionato)

    # Mediana de roubo_veiculo - Divide a distribuição em duas partes iguais
    mediana_estelionato = np.median(array_estelionato)
    
    
    distancia = abs((media_estelionato - mediana_estelionato)/mediana_estelionato *100)

    print(f'Média de estelionato: {media_estelionato}')
    print(f'Mediana de estelionato: {mediana_estelionato}')
    print(f'Diferença entre média e mediana {distancia: .2f}%')

except Exception as e:
    print(f'Erro ao obter informações sobre padrão de estelionato: {e}')
    exit()
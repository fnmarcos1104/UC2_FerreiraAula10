import os

os.system('cls')

import pandas as pd 
import matplotlib.pyplot as plt

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

    maximo = np.max(array_estelionato)
    minimo = np.min(array_estelionato)
    amplitude = maximo - minimo

    q1 = np.quantile(array_estelionato, 0.25, method='weibull')
    q2 = np.quantile(array_estelionato, 0.50, method='weibull')
    q3 = np.quantile(array_estelionato, 0.75, method='weibull')

    iqr = q3 - q1

    limite_superior = q3 + (1.5 * iqr)
    limite_inferior = q1 - (1.5 * iqr)


    print(f'Média de estelionato: {media_estelionato}')
    print(f'Mediana de estelionato: {mediana_estelionato}')
    print(f'Diferença entre média e mediana {distancia: .2f}%')

    print(media_estelionato)
    print(mediana_estelionato)
    print(distancia)

    print('\nMEDIDAS DE DISPERSÃO:')
    print(30*'-')
    print('\nMÍNIMO: ', minimo)
    print(f'Limite Inferior: {limite_inferior:.2f}')
    print('Q1 (25%): ', q1)
    print('Q2 (50%): ', q2)
    print('Q3 (75%): ', q3)
    print(f'IQR: {iqr:.2f}')
    print(f'Limite Superior: {limite_superior:.2f}')
    print(f'MÁXIMO: ', maximo)
    print('\nMunicípios com outliers inferiores:')
    print(30*'-')

except Exception as e:
    print(f'Erro ao obter informações sobre padrão de estelionato: {e}')
    exit()



try:
    # print(df_roubo_veiculo)
    plt.subplots(1, 2, figsize=(16, 7))
    plt.suptitle('Análise de roubo de veículos no RJ')

    plt.subplot(1, 2, 1)
    plt.boxplot(array_estelionato, vert=False, showmeans=True, showfliers=True)
    plt.title('Boxplot dos Dados')

    # Segunda subplot: Exibição de informações estatísticas
    plt.subplot(1, 2, 2)  # Configurar o segundo gráfico no lado direito
    plt.text(0.1, 0.9, f'Média: {media_estelionato}', fontsize=12)
    plt.text(0.1, 0.8, f'Mediana: {mediana_estelionato}', fontsize=12)
    plt.text(0.1, 0.7, f'Distância: {distancia}', fontsize=12)
    plt.text(0.1, 0.6, f'Menor valor: {minimo}', fontsize=12) 
    plt.text(0.1, 0.5, f'Limite inferior: {limite_inferior}', fontsize=12)
    plt.text(0.1, 0.4, f'Q1: {q1}', fontsize=12)
    plt.text(0.1, 0.3, f'Q3: {q3}', fontsize=12)
    plt.text(0.1, 0.2, f'Limite superior: {limite_superior}', fontsize=12)
    plt.text(0.1, 0.1, f'Maior valor: {maximo}', fontsize=12)
    plt.text(0.1, 0.0, f'Amplitude Total: {amplitude}', fontsize=12)
    plt.title('Medidas Observadas')

    # Desativar os eixos
    plt.axis('off')

    # Ajustar layout
    plt.tight_layout()

    plt.show()

except ImportError as e:
    print(f'Erro ao visualizar dados: {e}')
    exit()
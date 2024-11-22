import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# obter dados
try:
    print('Obtendo dados...')
    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    # utf-8, iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(
        ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # demilitando somente as variáveis de delegacia
    df_recup_veiculo = df_ocorrencias[['cisp', 'recuperacao_veiculos']]

    # Totalizando por delegacia
    df_recup_veiculo = df_recup_veiculo.groupby(
        ['cisp']).sum(['recuperacao_veiculos']).reset_index()

    print(df_recup_veiculo.head())
    print('Dados obtidos com sucesso!')

except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()

# Distribuição dos dados
try:
    print('Descrevendo a distribuição dos dados...')
    # Converter para um array numpy
    array_recup_veiculo = np.array(df_recup_veiculo['recuperacao_veiculos'])

    # Medidas de Tendência Central
    media = np.mean(array_recup_veiculo)
    mediana = np.median(array_recup_veiculo)
    distancia_media_mediana = (media-mediana)/mediana

    # Medidas de Posição e Dipersão
    q1 = np.quantile(array_recup_veiculo, 0.25, method='weibull')
    q3 = np.quantile(array_recup_veiculo, 0.75, method='weibull')
    iqr = q3 - q1
    minimo = np.min(array_recup_veiculo)
    limite_inferior = q1 - (1.5*iqr)
    limite_superior = q3 + (1.5*iqr)
    maximo = np.max(array_recup_veiculo)
    amplitute_total = maximo - minimo

    # Prints Medidas de Tendência Central
    print('\nMedidas de Tendência Central')
    print(30*'-')
    print(f'Média: {media}')
    print(f'Mediana: {mediana}')
    print(f'Distância média da mediana: {distancia_media_mediana:.2f}')

    # Prints Medidas Posição e Dispersão
    print('\nMedidas de Posição e Dispersão')
    print(30*'-')
    print(f'Menor valor: {minimo}')
    print(f'Limite inferior: {limite_inferior}')
    print(f'Q1: {q1}')
    print(f'Q3: {q3}')
    print(f'Limite superior: {limite_superior}')
    print(f'Maior valor: {maximo}')
    print(f'IQR: {iqr}')
    print(f'Amplitude total: {amplitute_total}')

    # Pegar as DPs com outliers superiores
    df_recup_veiculo_outliers_sup = df_recup_veiculo[
        df_recup_veiculo['recuperacao_veiculos'] > limite_superior]

    print('\nDPs com recuperações superiores as demais:')
    print(30*'-')
    if len(df_recup_veiculo_outliers_sup) == 0:
        print('Não existem DPs com valores discrepantes supreiores')
    else:
        print(df_recup_veiculo_outliers_sup.sort_values(
            by='recuperacao_veiculos', ascending=False))

    # Pegar as DPs com outliers inferiores
    df_recup_veiculo_outliers_inf = df_recup_veiculo[
        df_recup_veiculo['recuperacao_veiculos'] < limite_inferior]

    print('\nDPs com recuperações inferiores as demais:')
    print(30*'-')
    if len(df_recup_veiculo_outliers_inf) == 0:
        print('Não existem DPs com valores discrepantes inferiores')
    else:
        print(df_recup_veiculo_outliers_inf.sort_values(
            by='recuperacao_veiculos', ascending=True))

    # DPS que menos recuperaram veículos
    df_recup_veiculo_q1 = df_recup_veiculo[df_recup_veiculo['recuperacao_veiculos'] < q1]

    print('\nDPs que menos recuperaram veículos:')
    print(30*'-')
    print(df_recup_veiculo_q1.sort_values(
        by='recuperacao_veiculos', ascending=True))

except Exception as e:
    print(f'Erro ao descrever os dados: {e}')
    exit()


try:
    print('Caulculando medidas de distribuição...')

    # Caulculando Assimetria
    assimetria = df_recup_veiculo['recuperacao_veiculos'].skew()

    # Calculando Curtose
    curtose = df_recup_veiculo['recuperacao_veiculos'].kurtosis()

    print('\nMedidas de distribuição: ')
    print(30*'-')
    print(f'Assimetria: {assimetria}')
    print(f'Curtose: {curtose}')




except Exception as e:
    print(f'Erro ao calcular medidas de distribuição: {e}')
    exit()



try:
    # print(df_roubo_veiculo)
    plt.subplots(2, 2, figsize=(16, 7))
    plt.suptitle('Análise de recuperção de veículos no RJ')

    plt.subplot(2, 2, 1)
    plt.boxplot(array_recup_veiculo, vert=False, showmeans=True, showfliers=True)
    plt.title('Boxplot dos Dados')

    # SEGUNDA POSIÇÃO
    # Histograma
    plt.subplot(2, 2, 2)
    plt.hist(array_recup_veiculo, bins=50, edgecolor='black')
    plt.axvline(media, color='g', linewidth=1)
    plt.axvline(media, color='y', linewidth=1)



    # Segunda subplot: Exibição de informações estatísticas
    plt.subplot(2, 2, 3)  # Configurar o segundo gráfico no lado direito
    plt.text(0.1, 0.9, f'Média: {media}', fontsize=12)
    plt.text(0.1, 0.8, f'Mediana: {mediana}', fontsize=12)
    plt.text(0.1, 0.7, f'Distância: {distancia_media_mediana}', fontsize=12)
    plt.text(0.1, 0.6, f'Menor valor: {minimo}', fontsize=12) 
    plt.text(0.1, 0.5, f'Limite inferior: {limite_inferior}', fontsize=12)
    plt.text(0.1, 0.4, f'Q1: {q1}', fontsize=12)
    plt.text(0.1, 0.3, f'Q3: {q3}', fontsize=12)
    plt.text(0.1, 0.2, f'Limite superior: {limite_superior}', fontsize=12)
    plt.text(0.1, 0.1, f'Maior valor: {maximo}', fontsize=12)
    plt.text(0.1, 0.0, f'Amplitude Total: {amplitute_total}', fontsize=12)
    plt.title('Medidas Observadas')

    # Quarta posição
    plt.subplot(2, 2, 4)
    plt.text(0.1, 0.9, f'Variância: {variancia}'fontsize=12)
    plt.text(0.1, 0.8, f'Distância var x media: {distancia_var_media}'fontsize=12)
    plt.text(0.1, 0.7, f'Desvio Padrão: {desvio_padrao}'fontsize=12)
    plt.text(0.1, 0.6, f'Coef. variação: {coef_variacao}'fontsize=12)
    # Assimetria de curtose
    plt.text(0.1, 0.5, f'Assimetria: {assimetria}'fontsize=12)
    plt.text(0.1, 0.4, f'Curtose: {curtose}'fontsize=12)
    plt.title('Impressão de medidas estatisticas')

    # Desativar os eixos
    plt.axis('off')

    # Ajustar layout
    plt.tight_layout()

    plt.show()

except ImportError as e:
    print(f'Erro ao visualizar dados: {e}')
    exit()
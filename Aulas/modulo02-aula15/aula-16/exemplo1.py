import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ENDEREÇO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# CARREGANDO OS DADOS
try:
    df_ocorrencias = pd.read_csv(ENDEREÇO_DADOS, sep=';', encoding='latin1')
    
    #delimitando as variaves "cisp", "roubo_veiculo" e "recuperacao_veiculo"
    df_ocorrencias = df_ocorrencias[['cisp', 'roubo_veiculo', 'recuperacao_veiculos']]
    
    #agrupar por cisp e totalizar roubos e recuperações de veículos
    df_totalveiculos = df_ocorrencias.groupby('cisp', as_index=False)[['roubo_veiculo', 'recuperacao_veiculos']].sum()
   
    print(df_totalveiculos.head(10))

except Exception as e:
    print(f"Erro ao carregar os dados: {e}")

try:
    correlacao = np.corrcoef(df_totalveiculos['roubo_veiculo'], df_totalveiculos['recuperacao_veiculos'])[0,1]
    print(f"Correlação entre roubo de veículos e recuperação de veículos: {correlacao:.2f}")

except Exception as e:
    print(f"Erro ao calcular a correlação: {e}")


try:
    #plotando gráfico de dispersão
    plt.scatter(df_totalveiculos['roubo_veiculo'], df_totalveiculos['recuperacao_veiculos'])
    plt.title(f'Correlação entre roubo de veículos e recuperação de veículos: {correlacao:.2f}')
    plt.xlabel('Roubo de veículos')
    plt.ylabel('Recuperação de veículos')
    plt.show()

except Exception as e:
    print(f"Erro ao plotar o gráfico: {e}")
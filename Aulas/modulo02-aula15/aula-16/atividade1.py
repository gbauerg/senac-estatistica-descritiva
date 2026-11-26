import pandas as pd
import numpy as np

ENDEREÇO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# CARREGANDO OS DADOS
try:
    df_ocorrencias = pd.read_csv(ENDEREÇO_DADOS, sep=';', encoding='latin1')
    
    #delimitando as variaves "cisp", "roubo_veiculo" e "recuperacao_veiculo"
    df_ocorrencias = df_ocorrencias[['cisp', 'lesao_corp_morte', 'lesao_corp_dolosa']]

    #agrupar por cisp e totalizar roubos e recuperações de veículos
    df_lesao = df_ocorrencias.groupby('cisp', as_index=False)[['lesao_corp_morte', 'lesao_corp_dolosa']].sum()
   
    print(df_lesao.head(10))

except Exception as e:
    print(f"Erro ao carregar os dados: {e}")

try:
    correlacao = np.corrcoef(df_lesao['lesao_corp_morte'], df_lesao['lesao_corp_dolosa'])[0,1]
    print(f"Correlação entre Lesão seguida de Morte e Lesão Dolosa: {correlacao}")
    
except Exception as e:
    print(f"Erro ao calcular a correlação: {e}")

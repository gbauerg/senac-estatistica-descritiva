import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# obtendo os dados
try:
    print("Obtendo os dados...")

    ENDEREÇO_DADOS = "https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv"

    #utf-8, iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDEREÇO_DADOS, sep=";", encoding="cp1252")
    #print(df_ocorrencias)

    df_ocorrencias = df_ocorrencias[df_ocorrencias["regiao"] == "Interior"]

    #Delimitando os dados
    df_roubo_veiculos = df_ocorrencias[["munic", "roubo_veiculo"]]
    #print(df_roubo_veiculos.head(30))
    #print(df_roubo_veiculos.tail(30))
    
    #totalizando os roubos por cidade (Variável qualitativa "munic" e Variavel quantitatival "roubo_veiculo")
    df_roubo_veiculos = df_roubo_veiculos.groupby("munic", as_index=False)["roubo_veiculo"].sum()

    #Ordenando os dados
    df_roubo_veiculos = df_roubo_veiculos.sort_values(
        by="roubo_veiculo", ascending=False
    )

    total_roubos = df_roubo_veiculos['roubo_veiculo'].sum()
    
    df_roubo_veiculos['percentual'] = round((df_roubo_veiculos['roubo_veiculo'] / total_roubos) *100, 2)
    print(df_roubo_veiculos.tail(10))

except Exception as e:
    print(f"Erro ao obter os dados: {e}")

try:
    print(f"\nObtendo informações a cerca de roubos dos veículos...")
    array_roubo_veiculo = np.array(df_roubo_veiculos['roubo_veiculo'])

    print(f"\nMedidas de Tendência Central")
    
    media_roubo = np.mean(array_roubo_veiculo)
    print(f"Média: {media_roubo}")

    mediana_roubo = np.median(array_roubo_veiculo)
    print(f"Mediana: {mediana_roubo}")

    distancia = abs(
        (media_roubo - mediana_roubo) / mediana_roubo * 100
        )
    print(f"Distância: {distancia:.2f}%")


except Exception as i:
    print(f"Obtendo medidas - {i}")

try:

    q1 = np.quantile(array_roubo_veiculo, .25)
    q2 = np.quantile(array_roubo_veiculo, .50)
    q3 = np.quantile(array_roubo_veiculo, .75)

    print(f"\nMedidas de Posição")
    print(f"Q1: {q1}")
    print(f"Q2: {q2}")
    print(f"Q3: {q3}")

    df_roubo_veiculos_menores = df_roubo_veiculos[
        df_roubo_veiculos["roubo_veiculo"] < q1
    ]

    df_roubo_veiculos_maiores = df_roubo_veiculos[
        df_roubo_veiculos["roubo_veiculo"] > q3
    ]

    print(f"\nMunicipios com os Menores Roubos:")
    print(30*"=")
    print(df_roubo_veiculos_menores.sort_values(by="roubo_veiculo", ascending=True))
    df_roubo_veiculos_menores.to_csv("menores.csv", index=False, sep=";", encoding="cp1252")


    print(f"\nMunicipios com os Maiores Roubos:")
    print(30*"=")
    print(df_roubo_veiculos_maiores.sort_values(by="roubo_veiculo", ascending=False))
    df_roubo_veiculos_menores.to_csv("maiores.csv", index=False, sep=";", encoding="cp1252")

except Exception as j:
    print(f"Erro ao calcular os quartis {j}")

try:
    #Variância é a média dos quadrados das diferenças entre cada valor e a media
    variancia = np.var(array_roubo_veiculo)
    print(f"\nVariância: {variancia:.2f}")

    distancia_var_media = variancia / (media_roubo**2) *100
    print(f"Distância da Variância Média: {distancia_var_media:.2f}")

    desvio_padrao = np.std(array_roubo_veiculo)

    print(f"Desvio Padrão: {desvio_padrao:.2f}")

    coef_variação = (desvio_padrao / media_roubo)* 100
    print(f"Coeficiente de Variação: {coef_variação:.0f}%")


except Exception as m:
    print(f"Erro ao calcular a variabilidade do conjunto {m}")

try:
    iqr = q3 - q1
    print(iqr)

    lim_superior = q3 + (1.5 * iqr)
    lim_inferior = q1 - (1.5 * iqr)

    maximo = np.max(array_roubo_veiculo)
    minimo = np.min(array_roubo_veiculo)
    amplitude = maximo - minimo

    print(f"\nLimite Superior: {lim_superior}") 
    print(f"Limite Inferior: {lim_inferior}")  

    df_roubo_veiculos_outliers_menores = (df_roubo_veiculos[df_roubo_veiculos["roubo_veiculo"] < lim_inferior])
    print(df_roubo_veiculos_outliers_menores)

    print("\nMunicipios com Outliers Inferiores:")
    print(30*"-")
    if len(df_roubo_veiculos_outliers_menores) == 0:
        print("Não há outliers inferiores.")
    else:
        print(df_roubo_veiculos_outliers_menores)


    df_roubo_veiculos_outliers_maiores = (df_roubo_veiculos[df_roubo_veiculos["roubo_veiculo"] > lim_superior])
    print(df_roubo_veiculos_outliers_maiores)

    print("\nMunicipios com outliers superiores:")
    print(30*"-")

    if len(df_roubo_veiculos_outliers_maiores) == 0:
        print("Não há outliers superiores.")
    else:
        print(df_roubo_veiculos_outliers_maiores)

except Exception as n:
    print(f"Erro ao calcular outliers {n}")

try:
#indica como os dados estão distribuidos. para que lado tende a distribuicao
   
    #assimetria > 1
    #positiva alta
    #cauda longa a direita
    #Existem valores altos puxando a média pra cima
    #a media tende a ser maior que a mediana

    #Assimetria entre 0.5 e 1
    #positiva moderada
    #caudade existe mas menos acentuada
    #A média tende a ser maior que a mediana

    #Assimetria entre -0.5 e 0.5
    #tendencia a simetria
    #dados equilibrados em torno do centro
    #A média tende a ser próxima a mediana e a moda

    #Assimetria entre -1 e -0.5
    #negativa moderada
    #cauda existe, mas é menos acentuada
    #A média tende a ser menor que a mediana

    #assimetria < -1
    #negativa alta
    #cauda longa a esquerda
    #Existem valores baixos puxando a média pra baixo
    #a media tende a ser menor que a mediana

    assimetria = df_roubo_veiculos['roubo_veiculo'].skew()

    print(f"\nAssimetria: {assimetria}")
    
    #curtose
    #medida que verifica o peso das caudas
    #importancia dos valores extremos
    #quanto maior a curtose, maior tende a ser a influência dos extremos
    #referencia: cálculo de Fisher - Excesso de Curtose

    #-0.5 a 0.5 (Aproximadamente Mesocúrtica)
    #Curtose Próxima de uma distribuição normal.
    #Outliers não são comuns

    #curtose > 0.5 (Leptocúrtica)
    #Pode apresentar picos muito altos
    #Outliers mais frequentes


    #Curtose < -0.5 (Platicurtica)
    #Caudas mais leves. Menor Influencia dos extremos

    curtose = df_roubo_veiculos['roubo_veiculo'].kurtosis()

    print(f"Curtose: {curtose}")



except Exception as e:
    print(f"Erro ao calcular a Assimetria dos Dados")




try:
    print('\nInformações de Roubos de Veículos')
    plt.figure(figsize=(16, 10))


    # Posição 01 - Boxplot
    plt.subplot(2, 2, 1)

    plt.boxplot(df_roubo_veiculos['roubo_veiculo'], orientation='horizontal', showmeans=True, showfliers=False)
    plt.title('Distribuição dos dados')
    plt.xlabel('Roubo de Veículos')

    plt.subplot(2, 2, 2)
    plt.text(0.1, 0.95, f'Limite Inferior: {lim_inferior}', fontsize=12)
    plt.text(0.1, 0.90, f'Mínimo: {minimo}', fontsize=12)
    plt.text(0.1, 0.85, f'Q1: {q1}', fontsize=12)
    plt.text(0.1, 0.80, f'Q2: {q2}', fontsize=12)
    plt.text(0.1, 0.75, f'Q3: {q3}', fontsize=12)
    plt.text(0.1, 0.70, f'Limite Superior: {lim_superior}', fontsize=12)
    plt.text(0.1, 0.65, f'Máximo: {maximo}', fontsize=12)

    plt.text(0.1, 0.55, f'Mediana: {mediana_roubo}', fontsize=12)
    plt.text(0.1, 0.50, f'Média: {media_roubo}', fontsize=12)
    plt.text(0.1, 0.45, f'IQR Intervalo Interquartil: {iqr}', fontsize=12)
    plt.text(0.1, 0.40, f'Amplitude Total: {amplitude}', fontsize=12)
    plt.text(0.1, 0.35, f'Distância: {distancia}', fontsize=12)
    plt.axis('off')
    

    plt.subplot(2, 2, 3)
    
    plt.hist(array_roubo_veiculo, bins=100, edgecolor="black")
    plt.axvline(media_roubo, color="green", linewidth=1)
    plt.axvline(mediana_roubo, color="orange", linewidth=1)

    contagens, limite = np.histogram(array_roubo_veiculo, bins=100)
    
    print(f"\nFaixas de Roubos do Histograma")
    
    for i in range(len(contagens)):
        if contagens[i] > 0:
            print(
                f"Faixa {i+1}: "
                f"{limite[i]:.0f} até {limite[i+1]:.0f} roubos "
                f"=> {contagens[i]} Municípios"
            )


    plt.subplot(2, 2, 4)

    df_roubo_veiculos_maiores_10 = (df_roubo_veiculos_maiores.head(10).sort_values(by='roubo_veiculo', ascending=True))
    
    plt.bar(df_roubo_veiculos_maiores_10['munic'], df_roubo_veiculos_maiores_10['roubo_veiculo'])
    plt.xlabel("Municípios")
    plt.ylabel("Roubos")
    plt.xticks(rotation=45, ha= "right")


    plt.title("Top 10 - Municipios com mais roubos")

    plt.suptitle('Informações sobre Roubos de Veículos') 

    plt.show()

except Exception as e:
    print(f'Erro ao plotar o grafico: {e}')
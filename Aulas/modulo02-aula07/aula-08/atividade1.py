import pandas as pd
import numpy as np
import subprocess

subprocess.run("cls", shell=True)

try:
    print("Obtendo Dados...")

    ENDEREÇO_DADOS = "https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv"

    df_ocorrencias = pd.read_csv(ENDEREÇO_DADOS, sep=";", encoding="cp1252")

    df_estelionatos = df_ocorrencias[["mes_ano", "estelionato"]]

    df_estelionatos = df_estelionatos.groupby("mes_ano", as_index=False)["estelionato"].sum()
    df_estelionatos = df_estelionatos.sort_values(by="estelionato", ascending=False)
    
    print(df_estelionatos.tail(30))

except Exception as e:
    print(f"Erro ao obter dados: {e}")

try:
    print(f"\nCalculando Dados")
    array_estelionatos = np.array(df_estelionatos["estelionato"])
    
    media = np.mean(array_estelionatos)
    print(f"Média: {media}")

    mediana = np.median(array_estelionatos)
    print(f"Mediana: {mediana}")

    distancia = abs((media - mediana) / mediana * 100)
    print(f"Distância: {distancia:.2f}")

except Exception as i:
    print(f"Erro ao Calcular medidas: {i}")


try:
    print(f"\nCalculando Quartis...")
    q1 = np.quantile(array_estelionatos, .25)
    q2 = np.quantile(array_estelionatos, .50)
    q3 = np.quantile(array_estelionatos, .75)

    print("Medidas de Posição")

    print(f"Q1 (abaixo de 25%): {q1}")
    print(f"Q2 (50%):: {q2}")
    print(f"Q3 (acima dos 75%): {q3}")

    df_estelionatos_menores = df_estelionatos[df_estelionatos["estelionato"] < q1]
    df_estelionatos_maiores = df_estelionatos[df_estelionatos["estelionato"] > q3]

    print(f"\nMeses com os menores quantidades de Estelionatos: ")
    print(30*"=")
    menor = df_estelionatos_menores.sort_values(by="estelionato", ascending=True)
    print(menor.head(10))

    print(f"\nMeses com os maiores quantidades de Estelionatos: ")
    print(30*"=")
    maior = df_estelionatos_maiores.sort_values(by="estelionato", ascending=False)
    print(maior.head(10))
          
except Exception as j:
    print(f"Erro ao calcular quartis: {j}")

padrao = "\nDe acordo com o que foi mostrado, a distância elevada (53) mostra que não há padrão no número de ocorrências. "
print(padrao)


try:
    iqr = q3 - q1
    lim_superior = q3 + (1.5 * iqr)
    lim_inferior = q1 - (1.5 * iqr)

    print(f"\nLimite Superior: {lim_superior}")
    print(f"Limite Inferior: {lim_inferior}")

    df_estelionatos_outliers_maiores = (df_estelionatos[df_estelionatos["estelionato"] > lim_superior])
    print("\nMeses e anos com Outliers Maiores")
    if len(df_estelionatos_outliers_maiores) == 0:
        print("Não há outliers Superiores.")
    else:
        print(df_estelionatos_outliers_maiores)


    df_estelionatos_outliers_menores = (df_estelionatos[df_estelionatos["estelionato"] < lim_inferior])
    print("\nMeses e Anos com Outliers Inferiores")
    if len(df_estelionatos_outliers_menores) == 0:
        print("Não há outliers inferiores.")
    else:
        print(df_estelionatos_outliers_menores)

except Exception as o:
    print(f"Erro ao calcular os Outliers: {o}")
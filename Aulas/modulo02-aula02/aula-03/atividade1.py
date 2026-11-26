import pandas as pd
import subprocess
import numpy as np

subprocess.run("cls", shell=True)

df_moveis = pd.read_csv("C:/Users/gabriel.delgado/Documents/Análise de Dados/Dados/Aula 03/planilha_moveis.csv")

print(df_moveis.head(5))

df_moveis["Total Vendido"] = (
    df_moveis["Preco"] * df_moveis["Vendidos"]
)
print(df_moveis.head(5))

array_moveis = pd.array(df_moveis["Total Vendido"])

print("\nPadrão Central")
print(30*"=")

media = np.mean(array_moveis)
mediana = np.median(array_moveis)

#Quartil
q1 = np.quantile(array_moveis, .25)
q2 = np.quantile(array_moveis, .50)
q3 = np.quantile(array_moveis, .75)

print(f"Produtos abaixo dos 25%: {q1}.")
print(f"Padrão Central: {q2}")
print(f"Maior Representatividade Financeira (faixa dos 75% ou mais): {q3}")

interpretacao = "Minha interpretação foi de que, ao somar o valor dos produtos e quantidade vendida, teriamos o valor total. Com esse dado gerado, consigo obter as posições e o valor médio, que vão me trazer as respostas apresentadas na situação."
print(f"\n{interpretacao}")
import pandas as pd
import subprocess
import numpy as np


subprocess.run("cls", shell=True)

df_custos = pd.read_csv("C:/Users/gabriel.delgado/Documents/Análise de Dados/Dados/planilha_de_custos.csv")
print(df_custos.head())

df_custos["Preco Final (R$)"] = (
    df_custos["Preco de Compra (R$)"] +
    (df_custos["Preco de Compra (R$)"] * df_custos["Imposto (%)"] / 100) +
    df_custos["Frete (R$)"] +
    df_custos["Taxa Operacional (R$)"]
)
print("\nCusto Final")
print(df_custos[["Produto", "Preco Final (R$)"]].head())


array_custo = np.array(df_custos["Preco Final (R$)"])

media = np.mean(array_custo)
mediana = np.median(array_custo)

print("\nMedida de Tendência Central ")
print(f"Média: {media}")
print(f"Mediana: {mediana}")


import pandas as pd

df_vendas = pd.read_excel("C:/Users/gabriel.delgado/Documents/Análise de Dados/Dados/vendas_roupas.xlsx")

print(df_vendas.head(5))

print("\nTotal de unidades vendidas:")
print(df_vendas["Unidades Vendidas"].sum())

print(f"\nMaior Faturamento:")
maximo = df_vendas["Faturamento Total (R$)"].max()
print(df_vendas[df_vendas["Faturamento Total (R$)"] == maximo][["Produto", "Faturamento Total (R$)"]])

print(f"\nMenor Faturamento:")
minimo = df_vendas["Faturamento Total (R$)"].min()
print(df_vendas[df_vendas["Faturamento Total (R$)"] == minimo][["Produto", "Faturamento Total (R$)"]])

print(f"\nPreço Médio: {df_vendas["Preco por Unidade (R$)"].mean()}")

print(f"\nMenor Nível de Satisfação:") 
print(df_vendas[df_vendas["Satisfacao"] == "BAIXO"][["Produto", "Satisfacao"]])

print(f"\nMaior Nível de Satisfação:") 
print(df_vendas[df_vendas["Satisfacao"] == "MUITO ALTO"][["Produto", "Satisfacao"]])
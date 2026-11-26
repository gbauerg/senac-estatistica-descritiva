import pandas as pd

df_vendas = pd.read_excel("vendas_eletronicos.xlsx")

print(df_vendas.head(10))

#maior valor
print(f"\nMaior Faturamento:")
maximo = df_vendas["Faturamento Total (R$)"].max()
print(df_vendas[df_vendas["Faturamento Total (R$)"] == maximo][["Produto", "Faturamento Total (R$)"]])


print(f"\nMenor Faturamento")
minimo = df_vendas["Faturamento Total (R$)"].min()
print(df_vendas[df_vendas["Faturamento Total (R$)"] == minimo][["Produto", "Faturamento Total (R$)"]])


print(f"\nQuantidade Total de Unidades Vendidas: {df_vendas["Unidades Vendidas"].sum()}")
print(f"Preço Médio: {df_vendas["Preco por Unidade (R$)"].mean()}")

#media das unidades vendidas
media = df_vendas["Unidades Vendidas"].mean()
print(f"\nMédia de Unidades Vendidas: {media}")
print(df_vendas[df_vendas["Unidades Vendidas"] < media])
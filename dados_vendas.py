import pandas as pd

dados = pd.read_csv("DataSete/dados_venda.csv")
df = pd.DataFrame(dados)

media_vendas_anos = df.groupby("ano")["vendas"].mean()
print("A Media de Vendas por Ano:",media_vendas_anos)

media_vendas_produto = df.groupby("produto")["vendas"].mean()
print("A Media de Vendas por Produto:",media_vendas_anos)

media_vendas_lucros = df.groupby("produto")["lucro"].mean()
print("Media de Lucro por Produto:",media_vendas_lucros)

vendas_maiores_2000 = df[df["vendas"] > 2000]
print("Vendas Maiores que 2000:")
print(vendas_maiores_2000)
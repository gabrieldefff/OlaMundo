#%%
import pandas as pd
import os

print(os.getcwd())

#%%
lista_arquivos = os.listdir() #percorre e lista todo o diretório
lista_cidades2 = []
for arquivo in lista_arquivos:
    if ".xlsx" in arquivo: #do diretório seleciona somente os que possuem .xlsx
        nome_cidade = arquivo.replace("Loja ", "").replace(".xlsx", "")
        lista_cidades2.append(nome_cidade) # arquivo: Loja DF.xlsx

print(lista_cidades2)

#%%
lista_cidades = ["BH", "DF", "Manaus", "Rio", "Salvador", "SP"]

for cidade in lista_cidades:
    vendas_df = pd.read_excel(f"Loja {cidade}.xlsx") # df = dataframe
    print(vendas_df)
# %%
#teste
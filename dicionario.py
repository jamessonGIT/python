import streamlit as st
import pandas as pd
import csv



#carregando o arquivo CSV
arquivo_csv = "arquivo_dados.csv"
df=pd.read_csv(arquivo_csv, sep=";", encoding="latin1")

print(df.head())
dados = df.to_dict(orient="records")

print(dados[:1])

lista_dados = []
with open("arquivo_dados.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)  # Cada linha vira um dicionário
    for linha in reader:
        lista_dados.append(dict(linha))     




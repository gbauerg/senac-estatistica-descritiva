import pandas as pd
import polars as pl
import numpy as np
from datetime import datetime
import os

ENDERECO_DADOS = "./../DADOS/"

try:
    inicio = datetime.now()
    print("Obtendo os Dados do Bolsa Família")

    df_bolsafamilia = None
    lista_arquivos = []
    
    lista_dir_arquivos = os.listdir(ENDERECO_DADOS)
    for arquivo in lista_dir_arquivos:
        if arquivo.endswith('.csv'):
            lista_arquivos.append(arquivo)

    for arquivo in lista_arquivos:
        print(f"Processando o arquivo {arquivo}")
        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=";", encoding="iso8859-1")

        if df_bolsafamilia is None:
            df_bolsafamilia = df
        else:
            df_bolsafamilia = pl.concat([df_bolsafamilia, df])
        

        del df
        print(df_bolsafamilia.head())
        print(f"{arquivo} processado com sucesso!")


    print(f"Dados concatenados com sucesso.")

    df_bolsafamilia = df_bolsafamilia.with_columns(
        pl.col('VALOR PARCELA').str.replace(",", ".").cast(pl.Float64)
    )
    
    print(f"\nConvertendo em arquivo parquet")
    df_bolsafamilia.write_parquet("./../DADOS/bolsafamilia2026.parquet")
    print(f"Arquivo convertido com sucesso!")

    fim = datetime.now()
    print(f"Tempo Total: {fim-inicio}")

except Exception as e:
    print(f"Erro ao obter dados {e}")


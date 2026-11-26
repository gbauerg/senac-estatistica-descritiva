import polars as pl
import pandas as pd
from datetime import datetime

ENDERECO_DADOS = "./../DADOS/"

try:
    inicio = datetime.now()
    print(f"Obtendo Dados Parquet")

    df_bolsafamilia = pl.scan_parquet(ENDERECO_DADOS + "bolsafamilia2026.parquet")

    df_bolsafamilia = df_bolsafamilia.collect()
    print(df_bolsafamilia.head())

    fim = datetime.now()
    print(f"Tempo Total: {fim - inicio}")
except Exception as e:
    print(f"Erro ao obter dados {e}")
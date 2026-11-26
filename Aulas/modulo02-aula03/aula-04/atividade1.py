import pandas as pd
import subprocess
from sqlalchemy import create_engine

host = "localhost"
user = "root"
password = ""
database = "bd_aula04"

subprocess.run("cls", shell=True)

engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{host}/{database}"
)

query1 = "select * from materiais_construcao;"
query2 = "select produto, preco from materiais_construcao;"
query3 = "select * from materiais_construcao where categoria = 'cimento';"
query4 = "select * from materiais_construcao where preco > 200;"


df_materiais = pd.read_sql(query1, engine)
print("\nQuery 1")
print(df_materiais)

df_materiais = pd.read_sql(query2, engine)
print("\nQuery 2")
print(df_materiais)

df_materiais = pd.read_sql(query3, engine)
print("\nQuery 3")
print(df_materiais)

df_materiais = pd.read_sql(query4, engine)
print("\nQuery 4")
print(df_materiais)
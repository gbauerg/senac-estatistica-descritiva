import pandas as pd
from sqlalchemy import create_engine
import subprocess

# Variáveis de Conexão
host = "localhost"
user = "root"
password = ""
database = "bd_aula04"

subprocess.run("cls", shell=True)

# Criando a Conexão
engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{host}/{database}"
)

# Consultas
query = "select * from cadastro_produtos;"

query2 = "select * from cadastro_produtos where Marca = 'Hashtag' and `Preço Unitario` > 20;"

df_produtos = pd.read_sql(query2, engine)
print(df_produtos)



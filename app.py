import os
import dotenv
from pymongo.mongo_client import MongoClient
from pprint import pprint


env_file = ".env"
db_name = "geobr"
dotenv.load_dotenv(env_file)
URL=os.environ["db_url"]


def get_connection():
    client = MongoClient(URL)
    bases = list(client.list_databases()) # todas as bases
    # print(bases)
    db = client[db_name]
    return db
db = get_connection()
print(db.list_collection_names()) # base geobr

# executar o arquivo pelo terminal:
# python3 app.py

def get_municipios_estado(Uf):

    res = db.municipios.find({"Uf": Uf} , {"_id": 0, "Nome": 1})
    return (list(res)) 

# ATIVIDADES:

# 1 . Consulta todos os municipios do Acre

result = get_municipios_estado("AC")
pprint(f'total = {len(result)}')
pprint(result)

# 2 . Consulta todos os municipios de Roraima

result = get_municipios_estado("RR")
pprint(f'total = {len(result)}')
pprint(result)

# 3 . Consulta Municipios com o nome Cascavel, remover o _id do resultado



# 4 . Municipios que comecam com a letra W

# 5 . Municipios da Regiao Norte

# 6 . Ranking dos estados com maior quantidade de municipios
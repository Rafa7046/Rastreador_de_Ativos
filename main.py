import time
from google.cloud import datastore
import random

PROJECT_ID = 'rastreador-de-ativos'
ENTITY_KIND = 'AtivosFinanceiros' 

client = datastore.Client(project=PROJECT_ID)

def registrar_ativo(nome, preco):

    key = client.key(ENTITY_KIND, nome)

    entity = datastore.Entity(key=key)
    entity['nome'] = nome
    entity['preco'] = preco
    entity['timestamp'] = time.time()

    client.put(entity)

print("Iniciando o rastreador de ativos...")

while True:

    i = random.randint(10, 1000)
    ativo1 = {
        'nome': 'AAPL',
        'preco': i+140 
    }
    ativo2 = {
        'nome': 'GOOGL',
        'preco': i+1800.0 
    }
    ativo3 = {
        'nome': 'VALE3',
        'preco': i+55.0 
    }
    ativo4 = {
        'nome': 'BRKM3',
        'preco': i+32.0 
    }
    ativo5 = {
        'nome': 'UFAL',
        'preco': i+1000.0 
    }


    registrar_ativo(ativo1['nome'], ativo1['preco'])
    registrar_ativo(ativo2['nome'], ativo2['preco'])
    registrar_ativo(ativo3['nome'], ativo3['preco'])
    registrar_ativo(ativo4['nome'], ativo4['preco'])
    registrar_ativo(ativo5['nome'], ativo5['preco'])

    print(f"Ativos registrados: {ativo1['nome']}, {ativo2['nome']}")


    time.sleep(10) 

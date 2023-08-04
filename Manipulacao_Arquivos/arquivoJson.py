import json

# Lendo o arquivo JSON e manipulando ele
# with open("bd.json", "r") as arq_json:
#    dicionario = json.load(arq_json)
#    for chave, dados in dicionario.items():
#        print(chave + " | " + str(dados))

dicionario = {
    "CHAVES": ["CHAVES DO 8", "14/04/2017", "RECEP_01"],
    "QUICO": ["QUICO FLORES", "24/04/2017", "RAIOX_01"],
    "FLORINDA": ["DONA FLORINDA", "18/04/2017", "RECEP_03"]
}

# Inserindo dados no JSON
with open("bd.json", "w") as arq_json:
    json.dump(dicionario, arq_json)

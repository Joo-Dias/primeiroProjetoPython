# Criando um dicionário
usuarios = {}

# Colocando valores no dicionáro
usuarios = {
    "chaves" : ["Chaves do 8", "24/12/2017", "Recep_01"],
    "quico" : ["Quico das flores", "20/12/2017", "Raiox_03"]
}

# Colocando outro valor no dicionário dinamicamente
usuarios["florinda"] = ["Dona Florinda", "24/12/2017", "Raiox_01"]

print(usuarios)

print("=====")

# Pegando com o método GET apenas uma chave do dicionário
print(usuarios.get("chaves"))
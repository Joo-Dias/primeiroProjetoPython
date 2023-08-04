# Abrindo o arquvio iris.data para gravar os dados que desejo manipular e visualizar
baseDados = []

with open("iris.data", "r") as arquivo:
    for registro in arquivo.readlines():
        baseDados.append(registro.split(","))

print(baseDados)
print(baseDados[0][0])
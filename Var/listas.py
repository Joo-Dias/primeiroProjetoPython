# Criando uma variável do tipo LISTA[] para guardar várias informações

inventario = []
resposta = "S"

while resposta=="S":
    # Função APPEND() insere o dado na lista
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número serial: ")))
    inventario.append(input("Departamento: "))
    resposta = input("Digite 'S' para continuar: ").upper()

# Usando um laço FOR EACH para imprimir cada elemento da lista
for elemento in inventario:
    print(elemento)



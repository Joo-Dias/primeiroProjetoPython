inventario = []

escolhaMenu = "0"
respostaInserirDados = "S"

while escolhaMenu!="4":

    escolhaMenu = input("1 - Inserir Dados \n2 - Mostrar \n3 - Buscar \n4 - Finalizar \n:")

    if escolhaMenu == "1":
        while respostaInserirDados=="S":
            equipamento=[input("Equipamento: "),
                         float(input("Valor: ")),
                         int(input("Número serial: ")),
                         input("Departamento: ")]
            # Inserindo uma lista dentro da lista INVENTÁRIO
            inventario.append(equipamento)
            respostaInserirDados = input("Digite 'S' para continuar: ").upper()

        respostaInserirDados = "S"

    elif escolhaMenu == "2":

        # Variável para mostrar a ordem dos elementos
        indice = 0
        for elemento in inventario:
            indice = indice+1
            print("Índice: ", indice)
            print("Nome.........: ", elemento[0])
            print("Valor........: ", elemento[1])
            print("Serial.......: ", elemento[2])
            print("Departamento.: ", elemento[3])
            print("==========")

    elif escolhaMenu == "3":
        busca = input("Digite o nome do equipamento que deseja buscar: ")
        for elemento in inventario:
            if busca==elemento[0]:
                print("Nome.........: ", elemento[0])
                print("Valor........: ", elemento[1])
                print("Serial.......: ", elemento[2])
                print("Departamento.: ", elemento[3])

print("FIM!")




equipamentos = []
valores = []
seriais = []
departamentos = []

resposta = "S"
respostaMenu = "S"

# Criando um menu de escolha

while respostaMenu!="3":

    respostaMenu = input("1 - Inserir Dados\n2 - Busca\n3 - Finalizar\n")

    if respostaMenu=="1":
        while resposta=="S":
            equipamentos.append(input("Equipamento: "))
            valores.append(float(input("Valor: ")))
            seriais.append(int(input("Número serial: ")))
            departamentos.append((input("Departamento: ")))
            resposta = input("Digite 'S' para continuar: ").upper()

    elif respostaMenu=="2":
        # Procurando um item na lista por busca
        respostaBusca = "S"
        while respostaBusca=="S":
            busca = input("\nDigite o nome do equipamento que deseja buscar: ")
            for indice in range(0, len(equipamentos)):
                if busca==equipamentos[indice]:
                    print("\nNome.........: ", equipamentos[indice])
                    print("Valor........: ", valores[indice])
                    print("Serial.......: ", seriais[indice])
                    print("Departamento.: ", departamentos[indice])
                    respostaBusca = input("Deseja buscar outro item? ").upper()

    elif respostaMenu=="3":
        print("Fim do Programa!")
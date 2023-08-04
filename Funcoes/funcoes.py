# Para criar uma função utilizamos a palavra-chave DEF
def preencherLista(lista):
    resp="S"
    while resp=="S":
        equipamentos=[input("Equipamento: "),
                      float(input("Valor: ")),
                      int(input("Número Serial: ")),
                      input("Departamento: ")]
        lista.append(equipamentos)
        resp = input("Caso queira continuar digite 'S': ").upper()

def exibirLista(lista):
    for elemento in lista:
        print("Equipamento...: ", elemento[0])
        print("Valor.........: ", elemento[1])
        print("Serial........: ", elemento[2])
        print("Departamento..: ", elemento[3])
        print("==========")

def buscarPorEquipamentoLista(lista):
    busca = input("Digite o nome do equipamento: ")
    for elemento in lista:
        if busca == elemento[0]:
            print("Equipamento...: ", elemento[0])
            print("Valor.........: ", elemento[1])
            print("Serial........: ", elemento[2])
            print("Departamento..: ", elemento[3])
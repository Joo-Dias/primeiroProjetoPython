from Dicionarios.funcoesManageUsers import *

usuarios = {}

opcao = "OK"

while opcao!="SAIR":

    opcao = perguntar()

    if opcao=="I":
        inserir(usuarios)

    elif opcao=="P":
        pesquisar(usuarios)

    elif opcao=="E":
        excluir(usuarios)

print("FIM DO PROGRAMA!")
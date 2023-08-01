def perguntar():
    return input("O que deseja realizar?\n" +
              "<I> - Para inserir um usuário\n"+
              "<P> - Para pesquisar um usuário\n"+
              "<E> - Para excluir um usuário\n"+"<SAIR> - Para sair: ").upper()

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                   input("Digite a última data de acesso: ").upper(),
                                                   input("Digite a última estaçao acessada: ").upper()]

def pesquisar(dicionario):
    print(dicionario.get(input("Digite o login do usuario: ")))

def excluir(dicionario):
    chave = input("Digite a chave que deseja excluir: ")
    del dicionario[chave]

# Criando arquvios em python
# Colocando o nome e o modo de abertura do arquivo
#arquivo = open("primeiroArquivo.txt", "w")

# Escrevendo no arquivo
#arquivo.write("Meu primeiro arquivo!")

# Fechando o arquivo
#arquivo.close()

# Outra maneira de criar arquivo, uma maneira mais rapida e melhor
with open("primeiroArquivo.txt", "w") as arquivo:
    arquivo.write("\nHello World!")
usuarios = {}
emails = ["xpto@xyz.com", "xkcd@phd.com"]

# Numerando os emails com o método ENUMERATE e colocando numa lista
tupla = list(enumerate(emails))

# Laço de repetição para repetir até o tamanho da tupla
for chave in range(0, len(tupla)):
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave]] = [input("Digite o nome: "), input("Digite o nível de acesso: ")]

for chave, dado in usuarios.items():
    print("Usuário.:", chave[0])
    print("Email...:", chave[1])
    print("Nome....:", dado[0])
    print("Nível...:", dado[1])

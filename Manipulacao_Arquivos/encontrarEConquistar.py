texto = "Eu amo python!"

# Metodo para encontrar um caracter
print(texto.find("o"))

# Encontrando o outro "o"
print(texto[texto.find("o")+1:].find("o"))

# Cortando em pedacos o texto
print(texto.split(" "))
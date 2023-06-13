print("Hello World!")

# Variável do tipo String, Char...
# Método input() para inserir um valor
nome = input("Digite um nome: ")
empresa = input("Digite a instituição: ")

# Variável INT
qtde_funcionario = int(input("Digite a quantidade de funcionários: "))

# Variável FLOAT
mediaMensalidade = float(input("Digite a média da mensalidade: "))

print("========== Saídas ==========")

# Métodod print() para mostrar as variáveis
print(nome + " trabalha na empresa " + empresa)

# Utilizamos a ',' para indicar o fim do texto
print("A empressa possui", qtde_funcionario, "funcionários.")

# Método str() retorna uma representação do objeto em string
print("A média da mensalidade é de: " + str(mediaMensalidade))

print("========== Verifique os tipos de variáveis abaixo ==========")

# Método type() retorna o tipo da variável
print("O tipo de dado da VARIÁVEL [nome] é: ", type(nome))
print("O tipo de dado da VARIÁVEL [empresa] é: ", type(empresa))
print("O tipo de dado da VARIÁVEL [qtde_funcionario] é: ", type(qtde_funcionario))
print("O tipo de dado da VARIÁVEL [mediaMensalidade] é: ", type(mediaMensalidade))


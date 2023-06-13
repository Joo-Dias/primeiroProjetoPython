nome = input("Digite um nome: ")
idade = int(input("Digite uma idade: "))

# Estrutura de decisão IF
if idade >= 65:
    print("O paciente " + nome + " possui atendimento prioritário!")
else:
    print("O paciente " + nome + " não possui atendimento prioritário!")
print("FIM!")
nome = input("Digite um nome: ")
idade = int(input("Digite uma idade: "))

# Método uper() transforma o input da variável para caixa-maior(SIM)
doenca = input("Possui doença? ").upper()

# Estrutura de decisão IF
if idade >= 65:
    print("O paciente " + nome + " possui atendimento prioritário!")
elif doenca == "SIM":
    print("O paciente " + nome + " deve ser direcionado para a sala de espera reservada!")
else:
    print("O paciente " + nome + " não possui atendimento prioritário!")
print("FIM!")
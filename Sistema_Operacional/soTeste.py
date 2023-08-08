# Biblioteca nativa do python para conversar com o SO
import platform
from datetime import datetime
import getpass

print("Nome da maquina: ", platform.node())
print("Arquitetura: ", platform.architecture())
print("Sistema operacional: ", platform.system())
print("Versao do SO: ", platform.release())
print("Processador: ", platform.processor())
print("Versao do python: ", platform.python_version())

# Mostrando a data do SO
print(datetime.now())

# Retorna o usuario da maquina
print(getpass.getuser())

# Pede para inserir a senha
print(getpass.getuser("Digite sua senha: "))

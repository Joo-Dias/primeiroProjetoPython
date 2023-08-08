from ftplib import *

ftp = FTP("ftp.ibiblio.org")
print(ftp.getwelcome())

usuario = input("Digite o usuario: ")
senha = input("Digite a senha: ")

ftp.login(usuario, senha)

# Mostrando o diretorio atual
print("Diretorio atual de trabalho: ", ftp.pwd())

# Mudando o diretorio
ftp.cwd("pub")

print("Diretorio corrente: ", ftp.pwd())

# Comando que lista todos os arquivos que existe na pasta
print(ftp.retrlines("LIST"))

ftp.quit()
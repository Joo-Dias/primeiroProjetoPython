# Importando a biblioteca SOCKET para se comunicar com sistemas
import socket

resp = "S"
while resp=="S":
    url = input("Digite um URL: ")
    ip = socket.gethostbyname(url)
    print("O IP referente a URL e: ", ip)
    resp = input("Digite <S> para continuar: ").upper()
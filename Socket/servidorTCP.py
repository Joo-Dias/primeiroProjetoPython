from socket import *

servidor = "127.0.0.1" # localhost
porta = 43210

# Criando o objeto socket
obj_socket = socket(AF_INET, SOCK_STREAM)

# Configurando o servidor e a porta de entrada
obj_socket.bind((servidor, porta))

# Colocando o maximo de leitura do servidor
obj_socket.listen(2)

print("Aguardando cliente...")

while True:
    con, cliente = obj_socket.accept()
    print("Conectado com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024))
        print("Recebemos: ",msg_recebida)
        msg_enviada = b"Ola cliente"
        con.send(msg_enviada)
        break
    con.close()
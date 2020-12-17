import socket

client_socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = "127.0.0.1", 1234
client_socket.connect((host, port))
nom = input("Quelle est votre nom ?")
msg_send = True

if __name__ == "__main__":
    while True:
        message = input(f"{nom} >")
        client_socket.send(f"{nom} > {message}".encode("utf-8"))
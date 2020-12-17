import socket
import select

serveur = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host, port ="127.0.0.1", 1234
serveur.bind((host,port))
serveur.listen(4)
client_connectee = True
socket_objs = [serveur]

print("bienvenue dans le chat!!")

while client_connectee:
    liste_lu, liste_acce_Ecrit, exception = select.select(socket_objs, [], socket_objs)

    for socket_obj in liste_lu:

        if socket_obj is serveur:
            client, adresse = serveur.accept()
            print(f"l'objet client soket: {client} - adresse {adresse}")
            socket_objs.append(client)

        else:
            donnees_recus = socket_obj.recv(128).decode("utf-8")
            if donnees_recus:
                print(donnees_recus)

            else:
                socket_objs.remove(socket_obj)
                print("1 deco")
                print(f"{len(socket_objs) - 1} reste")
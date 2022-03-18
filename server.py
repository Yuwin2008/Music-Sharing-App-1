import socket
from threading import Thread

SERVER = None
IP_ADDRESS = "127.0.0.1"
PORT = 8050
clients = {}


def setup():
    print("\n\t\t\t\t\tIP MESSENGER\n")

    global SERVER
    global IP_ADDRESS
    global PORT

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(100)

    print("\t\t\t\t\tSERVER IS WAITING FOR INCOMING CONNECTIONS...\n")

    acceptConnections()


setupThread = Thread(target=setup)
setupThread.start()


def acceptConnections():
    global SERVER
    global clients

    while True:
        client, addr = SERVER.accept()
        print(client.addr)

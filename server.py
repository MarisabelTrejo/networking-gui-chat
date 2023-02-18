import socket
import threading

# IP address
HOST = "localhost"
PORT = 9090

# Connecting socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients = []
nicknames = []

# Broadcast, send messages
def broadcast(message):
    # Send messages to every client
    for client in clients:
        client.send(message)

# Handle individual connections
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            # Printing on the server
            print(f"{nicknames[clients.index(client)]}")
            # Sending to individual clients
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break

# Receive, accept new connections or clients
def recieve():
    while True:
        client, address = server.accept()
        print(f"Connecting with {str(address)}")

        # Work with client socket to send / communication
        client.send("NICKNAME".encode("utf-8"))

        # Append to the clients list
        clients.append(client)

        # Get the nickname from client
        nickname = client.recv(1024)
        nicknames.append(nickname)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} connected to the server!\n ".encode("utf-8"))

        # Send this message to this PARTICULAR client
        client.send("Connected to the server\n ".encode("utf-8"))

        thread = threading.Thread(target= handle, args=(client,))
        thread.start()

# meow
print("Server Running")
recieve()


    








        
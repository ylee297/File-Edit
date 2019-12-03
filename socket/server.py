# Imports modules
import socket
import time

listensocket = socket.socket()  # Creates an instance of socket
Port = 8000  # Port to host server on
maxConnections = 999
IP = socket.gethostname()  # IP address of local machine

listensocket.bind(("", Port))

# Starts server
listensocket.listen(maxConnections)
listOfClients
print("Server started at " + IP + " on port " + str(Port))

# Accepts the incomming connection
(clientsocket, address) = listensocket.accept()
print("New connection made => ", address)

running = True

with open("file.txt", "wb") as f:
    while running:
        data = clientsocket.recv(1024)  # Gets the incomming message
        print(data)
        if not data:
            continue
        f.seek(0)
        f.write(data)
        f.flush()

# # Imports library
# import socket

# # Creates instance of 'Socket'
# s = socket.socket()

# hostname = "Ivans-MacBook-Pro.local"  # Server IP/Hostname
# port = 5555  # Server Port

# s.connect((hostname, port))  # Connects to server

# while True:
#     x = input("Enter message: ")  # Gets the message to be sent
#     s.send(x.encode())  # Encodes and sends message (x)
import socket
import time
import threading

server = "Ivans-MacBook-Pro.local"
# server = "ivans-mbp.wifi.bcit.ca"
port = 8080

print(socket.gethostname())

clientOut = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientOut.connect((server, port))

clientIn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientIn.connect((server, port))


def fileListener():

    while True:
        print("innner thread (clientIn)")
        indata = clientIn.recv(1024)
        print("received")
        indata.decode()
        print(indata)


# threading.Thread(target=fileListener, args=()).start()

# try:
#     clientIn.bind(('', port))
# except socket.error as e:
#     str(e)
#
# try:
#     clientIn.listen()
# except socket.timeout:
#     print("timeout")
#     time.sleep(1)

# conn, address = clientIn.accept()
# print("second socket connected ", address)


while True:
    msg = input("send a message\n")
    if msg == "q":
        break
    clientOut.send(msg.encode())

clientOut.close()
clientIn.close()

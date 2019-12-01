
# select_echo_multiclient.py
import socket
import threading
import sys



server_address = ('localhost', 10000)
#socket write
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket read only
socketRead = sockIn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



# Create a TCP/IP socket

# Connect the socket to the port where the server is listening
print('connecting to {} port {}'.format(*server_address), file=sys.stderr)

sock.connect(server_address)
socketRead.connect(server_address)

def filelistener():
    while True:
        announcements = sock.recv(1024)
        localfile = open("localFile.txt", "wb")
        localfile.write(announcements)
        localfile.close()
        

#open another thread for a second socket.
#watch files that change
#send back keystrokes and file changes to the server and havev the server update the main file. then send it all back to the clients
#or sending back and forth files

threading.Thread(target=filelistener, args=()).start()

while True:
    keyboard = input("Type a message\n")

    if keyboard == 'exit':
        break

    outgoing_data = keyboard.encode()
    sock.send(outgoing_data)

    #data = sock.recv(1024)
    #print('{}: received {!r}'.format(sock.getsockname(), data), file=sys.stderr)

sock.close()


# for message in messages:
#     outgoing_data = message.encode()

#     # Send messages on both sockets
#     for s in socks:
#         print('{}: sending {!r}'.format(s.getsockname(), outgoing_data), file=sys.stderr)
#         s.send(outgoing_data)

#     # Read responses on both sockets
#     for s in socks:
#         data = s.recv(1024)
#         print('{}: received {!r}'.format(s.getsockname(), data), file=sys.stderr)
#         if not data:
#             print('closing socket', s.getsockname(), file=sys.stderr)
#             s.close()

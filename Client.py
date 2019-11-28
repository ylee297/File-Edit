
# select_echo_multiclient.py
import socket
import sys

server_address = ('localhost', 10000)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Create a TCP/IP socket

# Connect the socket to the port where the server is listening
print('connecting to {} port {}'.format(*server_address), file=sys.stderr)

sock.connect(server_address)

while True:
    keyboard = input("Type a message\n")

    if keyboard == 'exit':
        break

    outgoing_data = keyboard.encode()
    sock.send(outgoing_data)

    data = sock.recv(1024)
    print('{}: received {!r}'.format(sock.getsockname(), data), file=sys.stderr)

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

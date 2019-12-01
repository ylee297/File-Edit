# select_echo_server.py
import select
import socket
import sys
import queue


# list of clients
list_clients = []

# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address),
      file=sys.stderr)

server.bind(server_address)


# Listen for incoming connections
server.listen(5)


# Sockets from which we expect to read
inputs = [server]

#Second socket. each client has two sockets to the server.
#So everyone can write while server at the same time server writes out back to the clients
secondSocket = []

# Sockets to which we expect to write
outputs = []



#second socket 

# Outgoing message queues (socket:Queue)
message_queues = {}

while inputs:

    # Wait for at least one of the sockets to be
    # ready for processing
    # print('\nwaiting for the next event', file=sys.stderr)
    readable, writable, exceptional = select.select(inputs,
                                                    outputs,
                                                    inputs)
    # Handle inputs
    for s in readable:
        print('readable')
        # print('readable')
        if s is server:
            # A "readable" socket is ready to accept a connection
            print("two times")
            connection, client_address = s.accept()
            print('  connection from', client_address, file=sys.stderr)
            connection.setblocking(0)
            if( len(inputs)-1 == len(secondSocket)):
                inputs.append(connection)
            else:
                secondSocket.append(connection)

            # Give the connection a queue for data
            # we want to send
            message_queues[connection] = queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                # print('first')
                # A readable client socket has data
                # print('readable  received {!r} from {}'.format( data, s.getpeername()), file=sys.stderr, )
                file = open("client.txt", "ab")
                message_queues[s].put(data)

                # print(data.decode())
                file.write(data)

                file.close()
                # Add output channel for response
                if s not in outputs:
                    outputs.append(s)
            else:
                # Interpret empty result as closed connection
                print('  closing', client_address, file=sys.stderr)
                # Stop listening for input on the connection
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()

                # Remove message queue
                del message_queues[s]
    # Handle outputs
    for s in writable:
        print('writable2')
        try:
            next_msg = message_queues[s].get_nowait()
        except queue.Empty:
            # No messages waiting so stop checking
            # for writability.
            print('  ', s.getpeername(), 'queue empty', file=sys.stderr)
            outputs.remove(s)
        else:
            #            print('writable  sending {!r} to {}'.format(next_msg, s.getpeername()), file=sys.stderr)

            # send to every client
            file = open("client.txt", "r")
            for a in inputs:
                str = ''
                if a != server:
                    for line in file:
                        str += line+'\n'
                    a.send(str.encode())

            # s.send(next_msg)
            file.close()

            # print('writable4')
            # Handle "exceptional conditions"
    for s in exceptional:
        print('exception condition on', s.getpeername(),
              file=sys.stderr)
        # Stop listening for input on the connection
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()

        # Remove message queue
        del message_queues[s]

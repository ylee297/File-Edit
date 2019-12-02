import socket
import time
import threading

server = 'getip'
port = 5555

print(socket.gethostname())

clientOut = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientOut.connect((server, port))

clientIn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientIn.connect((server,port))

def fileListener():

    while True:
        print('innner thread (clientIn)')
        indata = clientIn.recv(1024)
        print('received')
        indata.decode()
        print(indata)


threading.Thread(target=fileListener , args=()).start()

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

#conn, address = clientIn.accept()
#print("second socket connected ", address)


while True:
    msg = input('send a message\n')
    if msg == 'q':
        break
    clientOut.send(msg.encode())

clientOut.close()
clientIn.close()
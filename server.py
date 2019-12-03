import socket
import threading
import time
from pyeditor import PyText
import tkinter as tk

editor = None


class Client_Thread(threading.Thread):
    def __init__(self, name, address, connection):
        threading.Thread.__init__(self)
        self.client_name = "Client" + str(name)
        self.address = address
        # same address
        self.socketIn = connection
        self.row = str(name) + ".0"
        self.id = name
        # self.socketOut = connection2

    def run(self):
        global editor
        print(self.name, " just joined! from ", self.address)
        data = ""
        with open("file.txt", "wb") as f:
            while True:
                data = self.socketIn.recv(2000)
                print("data:", data)

                # if self.socketI
                if data:
                    print("message from ", self.client_name)
                    f.write(data)
                    f.flush()
                    editor.textarea.delete(str(self.id) + ".0", str(self.id + 1) + ".0")
                    editor.textarea.insert(str(self.id) + ".0", data)
                else:
                    continue

        print(self.name, " disconnected from ", self.address)


class Server:
    def __init__(self):
        self.id = 1
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = ""
        self.port = 8000
        # how to fill this buffer
        self.buffer = []
        self.list_of_connections = []
        # self.editor = editor
        print(socket.gethostname())
        # threading.Thread(target=self.sendOut, args=()).start()

    # def sendOut(self):
    #     print('sendOut')
    #     while True:
    #         if self.buffer:
    #             for a in self.list_of_connections:
    #                 a.socketOut.send("hi".encode())
    #                 time.sleep(1)

    def get_list(self):
        return self.list_of_connections

    def connection_handler(self):
        try:
            self.s.bind((self.server, self.port))
        except socket.error as e:
            str(e)

        self.s.listen()
        print("Waiting for connection, Server Started")

        while True:
            conn, addr = self.s.accept()
            print("accept " + str(addr))
            # conn2, addr2 = self.s.accept()
            # print("accept " + str(addr2))
            t = Client_Thread(self.id, addr, conn)
            t.start()
            self.list_of_connections.append(t)
            self.id += 1


if __name__ == "__main__":
    # global editor
    root = tk.Tk()
    editor = PyText(root)
    server = Server()
    # server.connection_handler()
    threading.Thread(target=server.connection_handler).start()
    root.mainloop()


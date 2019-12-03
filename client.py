import threading
import tkinter as tk
from pyeditor import PyText
import socket
import time

editor = None


def watch():
    global editor
    # Creates instance of 'Socket'
    s = socket.socket()

    hostname = "Ivans-MacBook-Pro.local"  # Server IP/Hostname
    port = 8000  # Server Port

    s.connect((hostname, port))  # Connects to server

    while True:
        content = editor.textarea.get(1.0, tk.END)  # Gets the message to be
        bytes = content.encode(encoding="UTF-8")
        s.send(bytes)  # Encodes and sends message (x)
        print(bytes)
        time.sleep(1)


if __name__ == "__main__":
    root = tk.Tk()
    editor = PyText(root)
    threading.Thread(target=watch).start()
    root.mainloop()

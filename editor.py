import tkinter as tk
from tkinter import filedialog

root = tk.Tk("Text Editor")
text = tk.Text(root)
text.grid()


def saveas():
    global text
    t = text.get("1.0", "end-1c")
    file1 = open("file.txt", "w+")
    file1.write(t)
    file1.close()


button = tk.Button(root, text="Save", command=saveas)
button.grid()
root.mainloop()

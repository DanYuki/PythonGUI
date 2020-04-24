from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Dan's")
root.iconbitmap("assets/icon.ico")

appsMode = [
    ["Light", 1],
    ["Dark", 2],
]

modes = 1

Radiobutton(root, text=appsMode[0][0], variable=modes, value=appsMode[0][1], command=lambda: clicked(appsMode[0][1], appsMode[0][0])).pack()
Radiobutton(root, text=appsMode[1][0], variable=modes, value=appsMode[1][1], command=lambda: clicked(appsMode[1][1], appsMode[1][0])).pack()

def clicked(val, text):
    global valueOpt
    valueOpt.destroy()
    valueOpt = Label(root, text=text)
    valueOpt.pack()
    print(val)
    print(modes)

valueOpt = Label(root, text="None")
valueOpt.pack()

root.mainloop()

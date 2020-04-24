from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox, filedialog

#meta
root = Tk()
root.title("Dan's")
root.iconbitmap("assets/icon.ico")
root.geometry("400x400")

options = [
    "jpg",
    "png",
    "gif"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

root.mainloop()

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox, filedialog

#meta
root = Tk()
root.title("Dan's")
root.iconbitmap("assets/icon.ico")
root.geometry("400x400")

def show():
    Label(root, text=var.get()).pack()

var = StringVar()

check = Checkbutton(root, text="Check this box", variable=var, onvalue="On", offvalue="Off")
check.deselect()
check.pack() 

Label(root, text=var.get()).pack()

btn = Button(root, text="Show Value", command=show)
btn.pack()

root.mainloop()

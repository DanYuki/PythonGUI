from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Dan's")
root.iconbitmap("Ico/ico.ico")

frame = LabelFrame(root, text="This is frame", padx=50, pady=50)
frame.pack(padx=100, pady=100)

btn = Button(frame, text="Click here")
btn.pack()

root.mainloop()

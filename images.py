from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Dan's")
root.iconbitmap("Ico/ico.ico")

my_img = ImageTk.PhotoImage(Image.open("img/1.png"))
my_label = Label(image=my_img)
my_label.pack()


root.mainloop()

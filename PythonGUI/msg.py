from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

#meta
root = Tk()
root.title("Dan's")
root.iconbitmap("assets/icon.ico")

def popup():
    response = messagebox.askquestion("YAHALLO!", "Yo Wassup")
    print(response)
    if response == 'yes':
        Label(root, text="You Clicked yes!").pack()
    elif response == 'no':
        Label(root, text="You Clicked no!").pack()
Button(root, text="Popup", command=popup).pack()

root.mainloop()

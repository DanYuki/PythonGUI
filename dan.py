from tkinter import *

root = Tk()
inputBox = Entry(root)

def clicked():
    text = Button(root, text=inputBox.get(), state=DISABLED)
    text.pack()
    
#defining the comp
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is Dan Yuki!")
clickMe = Button(root, text="Click Me!", command = clicked, bg="blue", fg="white")

#placing the comp
clickMe.pack()
inputBox.pack()

root.mainloop()

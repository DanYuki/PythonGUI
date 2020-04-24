from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox, filedialog

#meta
root = Tk()
root.title("Dan's")
root.iconbitmap("assets/icon.ico")

def openImg():
    global img
    global content
    root.filename = filedialog.askopenfilename(initialdir="assets/img", title="Select a File", filetypes=(("Pict", "*.jpg"),("all files", "*.*")))
    if content != "":
        content.destroy()
    print(root.filename)    
    img = ImageTk.PhotoImage(Image.open(root.filename))
    content = Label(img_frame, image=img)
    content.pack()


img_frame = Frame(root, height=550, width=640)  
img_frame.pack()
content = Label(img_frame)
btn = Button(text="Open an Image", command=openImg)
btn.pack()

root.mainloop()

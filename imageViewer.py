from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Dan's")
root.iconbitmap("Ico/ico.ico")

#defining the var and widget
pos = 0
name = "img1"

img_prop = {
    "img1" : "ocean1.jpg",
    "img2" : "ocean2.jpg",
    "img3" : "ocean3.jpg",
    "img4" : "ocean4.jpg",
}

ocean1 = ImageTk.PhotoImage(Image.open("img/ocean1.jpg"))
ocean2 = ImageTk.PhotoImage(Image.open("img/ocean2.jpg"))
ocean3 = ImageTk.PhotoImage(Image.open("img/ocean3.jpg"))
ocean4 = ImageTk.PhotoImage(Image.open("img/ocean4.jpg"))

img_list = [ocean1, ocean2, ocean3, ocean4]

img_name = Label(root, text=f"{img_prop[name]}")
statusBar = Label(root, text=f"Image {pos + 1} of {len(img_list)}")

img_viewer = Label(image=img_list[pos])

#function sect

#changing the image
def img_init(pos):
    global img_viewer
    
    img_viewer.grid_forget()
    img_viewer = Label(image=img_list[pos])
    img_viewer.grid(row=0, column=0, columnspan=3)

def forward():
    global pos
    if pos == len(img_list) - 1:
        pos = 0
    else:
        pos += 1
    img_init(pos)
    status()
    imgName(pos)
    
def back():
    global pos
    if pos < 1:
        pos = len(img_list) - 1
    else:
        pos -= 1
    img_init(pos)
    status()
    imgName(pos)

#display the status bar
def status():
    statusBar.grid_forget()
    status = Label(root, text=f"Image {pos + 1} of {len(img_list)}")
    status.grid(row=2, column=1)

#display img name
def imgName(pos):
    global name
    global img_name
    if pos == 0:
        name = "img1"
    elif pos == 1:
        name = "img2"
    elif pos == 2:
        name = "img3"
    elif pos == 3:
        name = "img4"
    img_name.grid_forget()
    img_name = Label(root, text=f"{img_prop[name]}
                     ")
    img_name.grid(row=2, column=0)

#placing the widget                     
img_viewer.grid(row=0, column=0, columnspan=3)

button_back = Button(root, text="<<", command=back)
button_exit = Button(root, text="Exit Program", command=root.destroy)
button_forward = Button(root, text=">>", command=forward)

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

img_name.grid(row=2, column=0)
statusBar.grid(row=2, column=1)


root.mainloop()

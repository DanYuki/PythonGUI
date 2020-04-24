from tkinter import *

root = Tk()
root.title("Simple Calculator")

#variable_sect
insertedNumber = []
totalNum = 0

def addNumber(number):
    num=inputField.get()
    inputField.insert(len(num), number)
    
def operate(opt):
    if opt == "+" :
        insertedNumber.append(inputField.get())
        inputField.delete(0, END)
    elif opt == "=" :
        if inputField.get() == '':
            pass
        else:
            insertedNumber.append(inputField.get())
        inputField.delete(0, END)
        totalNum = 0 
        for i in insertedNumber:
            totalNum += int(i)
        insertedNumber.clear()
        inputField.insert(0, totalNum)

def clear():
    inputField.delete(0, END)
    
#defining the comp
inputField = Entry(root, width=35, borderwidth=5)
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: addNumber(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: addNumber(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: addNumber(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: addNumber(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: addNumber(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: addNumber(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: addNumber(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: addNumber(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: addNumber(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: addNumber(0))
button_add = Button(root, text="+", padx=39, pady=20, command=lambda: operate("+"))
button_equal = Button(root, text="=", padx=90, pady=20, command=lambda: operate("="))
button_clear = Button(root, text="Clear", padx=80, pady=20, command=clear)

#placing the comp
inputField.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

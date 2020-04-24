from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox, filedialog
import sqlite3

#meta
root = Tk()
root.title("Dan's")
root.iconbitmap("assets/icon.ico")
root.geometry("400x400")

#create or connect to db
conn = sqlite3.connect('address_book.db')

#create cursor
cur = conn.cursor()

#create table
'''
cur.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer)""")
'''
def submit():
    #create or connect to db
    conn = sqlite3.connect('address_book.db')

    #create cursor
    cur = conn.cursor()

    #insert into table
    cur.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
    {
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'address':address.get(),
        'city':city.get(),
        'state':state.get(),
        'zipcode':zipcode.get()
    })
    conn.commit()

    conn.close()

    #Clear text box
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

def query():
    #create or connect to db
    conn = sqlite3.connect('address_book.db')

    #create cursor
    cur = conn.cursor()

    cur.execute("SELECT *, oid FROM addresses")
    records = cur.fetchall()
    
    print(records)
    print_records = ""
    for x in records[2]:
        print_records += str(x) + "\n" 

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

    conn.commit()
    conn.close()

def delete():
    #create or connect to db
    conn = sqlite3.connect('address_book.db')

    #create cursor
    cur = conn.cursor()

    #delete record
    cur.execute("DELETE FROM addresses WHERE oid= " + delete_box.get())

    conn.commit()
    conn.close()

#Create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=30)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)

#Create text box labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Adresses")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(root, text="ID Number")
delete_box_label.grid(row=9, column=0)

#Create Submit btn
submit_btn = Button(root, text="Add Record to DB", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#Create Query btn
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#create delete btn
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

conn.commit()

conn.close()



root.mainloop()

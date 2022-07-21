from tkinter import *
import sqlite3
from tkinter import *

root = Tk()

conn = sqlite3.connect()

root.mainloop()

root = Tk()
root.geometry('400x500')

conn = sqlite3.connect('address_book.db')
c = conn.cursor()


def submit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("INSERT INTO addresses VALUES(:name, :surname, :address, :city, :state, :zipcode)",
              {
                  'name': name.get(),
                  'surname': surname.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })

    conn.commit()
    conn.close()

    name.delete(0, END)
    surname.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

def delete():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("DELETE from addresses WHERE oid = " + str(delete_box.get()))

    delete_box.delete(0, END)

    conn.commit()
    conn.close()


def query():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)
    print_records = ''

    for record in records:
        print_records += str(record[0]) + " " + str(record[6]) + '\n'

    myLabel = Label(root, text=print_records)
    myLabel.grid(row=12, column=0, columnspan=2)

    conn.commit()
    conn.close()


def edit():
    global name_editor, surname_editor, address_editor, city_editor, state_editor, zipcode_editor, record_id
    editor = Tk()
    editor.geometry('400x400')

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()

    print(records)
    print_records = ''

    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + '\n'

    name_editor = Entry(editor, width=30)
    surname_editor = Entry(editor, width=30)
    address_editor = Entry(editor, width=30)
    city_editor = Entry(editor, width=30)
    state_editor = Entry(editor, width=30)
    zipcode_editor = Entry(editor, width=30)

    name_editor.grid(row=0, column=1, padx=20)
    surname_editor.grid(row=1, column=1, padx=20)
    address_editor.grid(row=2, column=1, padx=20)
    city_editor.grid(row=3, column=1, padx=20)
    state_editor.grid(row=4, column=1, padx=20)
    zipcode_editor.grid(row=5, column=1, padx=20)

    f_name_label = Label(editor, text='Name:').grid(row=0, column=0, padx=20)
    f_surname_label = Label(editor, text='Surname:').grid(row=1, column=0, padx=20)
    address_label = Label(editor, text='Address:').grid(row=2, column=0, padx=20)
    city_label = Label(editor, text='City:').grid(row=3, column=0, padx=20)
    state_label = Label(editor, text='State:').grid(row=4, column=0, padx=20)
    zipcode_label = Label(editor, text='Zipcode:').grid(row=5, column=0, padx=20)

    ed_btn = Button(editor, text='Save Record', command=save).grid(row=6, column=0, columnspan=2, padx=10, pady=10,
                                                                ipadx=150)

    for record in records:
        name_editor.insert(0, record[0])
        surname_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])


def save():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("""UPDATE addresses SET
    first_name = :first,
    last_name = :last,
    address = :address,
    city = :city,
    state = :state,
    zipcode = :zipcode
    
    WHERE oid = :oid""",
    {
      'first': name_editor.get(),
      'last': surname_editor.get(),
      'address': address_editor.get(),
      'city': city_editor.get(),
      'state': state_editor.get(),
      'zipcode': zipcode_editor.get(),

      'oid': record_id
    })

    conn.commit()
    conn.close()


name = Entry(root, width=30)
surname = Entry(root, width=30)
address = Entry(root, width=30)
city = Entry(root, width=30)
state = Entry(root, width=30)
zipcode = Entry(root, width=30)
delete_box = Entry(root, width=30)

name.grid(row=0, column=1, padx=20)
surname.grid(row=1, column=1, padx=20)
address.grid(row=2, column=1, padx=20)
city.grid(row=3, column=1, padx=20)
state.grid(row=4, column=1, padx=20)
zipcode.grid(row=5, column=1, padx=20)
delete_box.grid(row=9, column=1, pady=5)

f_name_label = Label(root, text='Name:').grid(row=0, column=0, padx=20)
f_surname_label = Label(root, text='Surname:').grid(row=1, column=0, padx=20)
address_label = Label(root, text='Address:').grid(row=2, column=0, padx=20)
city_label = Label(root, text='City:').grid(row=3, column=0, padx=20)
state_label = Label(root, text='State:').grid(row=4, column=0, padx=20)
zipcode_label = Label(root, text='Zipcode:').grid(row=5, column=0, padx=20)
delete_box_label = Label(root, text='Delete ID:').grid(row=9, column=0, padx=20)

btn = Button(root, text='Add record to Database', command=submit).grid(row=6, column=0, columnspan=2, pady=10, padx=10)
q_btn = Button(root, text='Show Records', command=query).grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=140)
d_btn = Button(root, text='Delete Record', command=delete).grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=140)
e_btn = Button(root, text='Edit Record', command=edit).grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=150)

root.mainloop()
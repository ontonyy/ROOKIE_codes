from tkinter import *

root = Tk()
root.geometry('400x400')
e = Entry(root, width=50, bg='blue', fg='white', borderwidth=3)
e.pack()


def myClick():
    hello = f'Hello, {e.get()}!'
    myLabel = Label(root, text=hello)
    myLabel.pack()


btn = Button(root, text='Enter you full name', bg='cyan', fg='black', padx=30, command=myClick)
btn.pack()

root.mainloop()

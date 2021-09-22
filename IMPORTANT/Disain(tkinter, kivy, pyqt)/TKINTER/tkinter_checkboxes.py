from tkinter import *

root = Tk()


def show():
    myLabel = Label(root, text=var.get()).pack()

var = IntVar()
c = Checkbutton(root, text='Tested case', variable=var)
c.pack()
b = Button(root, text='Click', command=show).pack()
root.mainloop()
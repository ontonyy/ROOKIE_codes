from tkinter import *
from tkinter import messagebox

root = Tk()


def box():
    response = messagebox.askquestion('Do you really agree?', 'Really, REALLY AGREE?')
    Label(root, text=response)
    if response == "yes":
        m = messagebox.showinfo('FINE', 'FINE MAN')
        Label(root, text=m)
    while response == "no":
        r = messagebox.askquestion('Agreement', 'But now?')
        Label(root, text=r)
        if r == "yes":
            m = messagebox.showinfo('FINE', 'FINE MAN')
            Label(root, text=m)
            break

btn = Button(root, text='If agree CLICK!', command=box).pack()

root.mainloop()

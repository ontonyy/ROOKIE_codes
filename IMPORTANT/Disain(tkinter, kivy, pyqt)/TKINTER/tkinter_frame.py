from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Frame')


def btn_click():
    messagebox.showinfo(title='Сказали же...', message='Лан иди отсюдова уже, я устал и пошёл спать')


frame = LabelFrame(root, text='This is my field, enemy!', padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't click me here", command=btn_click)
b2 = Button(frame, text="...or here!", command=btn_click)

b.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()
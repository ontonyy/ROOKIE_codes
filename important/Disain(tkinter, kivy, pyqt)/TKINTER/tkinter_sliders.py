from tkinter import *

root = Tk()

vertical = Scale(root, from_=0, to=600)
vertical.pack()
horizontal = Scale(root, from_=0, to=600, orient=HORIZONTAL)
horizontal.pack()

def slide():
    global myLabel, myLabel2
    myLabel = Label(root, text=vertical.get()).pack()
    myLabel2 = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + 'x' + str(vertical.get()))

my_btn = Button(root, text='Click me!', command=slide).pack()

root.mainloop()
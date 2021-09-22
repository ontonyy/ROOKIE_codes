from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title('Second WINDOW opening')

def open():
    global myimg
    top = Toplevel()
    top.title('Second Window')
    myimg = ImageTk.PhotoImage(Image.open('../images/try1.png'))
    Label(top, image=myimg).pack()
    btn2 = Button(top, text='Close window', command=top.destroy).pack()

btn = Button(root, text='Open second WINDOW', command=open).pack()

mainloop()
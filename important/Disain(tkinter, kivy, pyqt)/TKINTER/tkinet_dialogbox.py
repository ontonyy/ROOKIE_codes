from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()


def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir='images', title='Select file', filetypes=(('png files', '*.png'), ('all files', '*.*')))
    mylabel = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_label_image = Label(root, image=my_image).pack()

btn = Button(root, text='Open File', command=open).pack()

root.mainloop()
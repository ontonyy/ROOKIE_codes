from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Funny picture')


def back(image_num):
    global mylabel, left_btn, right_btn
    mylabel.grid_forget()
    mylabel = Label(image=image_list[image_num + 1])
    left_btn = Button(root, text='<<', command=lambda: back(image_num - 1))
    right_btn = Button(root, text='>>', command=lambda: forward(image_num + 1))

    if image_num == -2:
        left_btn = Button(root, text='<<', state=DISABLED)

    status = Label(root, text=f'Image {str(image_num)} of {len(image_list)}', bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=1, columnspan=3, sticky=W + E)
    right_btn.grid(row=1, column=2)
    left_btn.grid(row=1, column=0)
    mylabel.grid(row=0, column=0, columnspan=3)


def forward(image_num):
    global mylabel, left_btn, right_btn
    mylabel.grid_forget()
    mylabel = Label(image=image_list[image_num - 1])
    right_btn = Button(root, text='>>', command=lambda: forward(image_num + 1))
    left_btn = Button(root, text='<<', command=lambda: forward(image_num - 1))
    right_btn.grid(row=1, column=2)
    mylabel.grid(row=0, column=0, columnspan=3)

    if image_num == 3:
        right_btn = Button(root, text='>>', state=DISABLED)

    status = Label(root, text=f'Image {str(image_num)} of {len(image_list)}', bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=1, columnspan=3, sticky=W + E)
    left_btn.grid(row=1, column=0)
    right_btn.grid(row=1, column=2)
    mylabel.grid(row=0, column=0, columnspan=3)


myimg = ImageTk.PhotoImage(Image.open("../images/try1.png"))
myimg2 = ImageTk.PhotoImage(Image.open("../images/try2.png"))
myimg3 = ImageTk.PhotoImage(Image.open("../images/try3.png"))

image_list = [myimg, myimg2, myimg3]

status = Label(root, text=f'Image 0 of {len(image_list)}', bd=1, relief=SUNKEN, anchor=E)
mylabel = Label(image=myimg)
right_btn = Button(root, text='>>', command= lambda: forward(1))
left_btn = Button(root, text='<<', command=lambda: back(1))
quit_pro = Button(text='Exit Program', command=root.quit)

status.grid(row=2, column=1, columnspan=5, sticky=W+E)
mylabel.grid(row=0, column=0, columnspan=3)
quit_pro.grid(row=1, column=1)
left_btn.grid(row=1, column=0)
right_btn.grid(row=1, column=2)

root.mainloop()
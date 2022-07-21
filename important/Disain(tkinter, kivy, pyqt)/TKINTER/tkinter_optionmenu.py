from tkinter import *

root = Tk()


def show():
    if int(clicked.get()) <= 3:
        myLabel2 = Label(root, text="You don't funny, funny").grid(row=2, column=0)
    if 3 < int(clicked.get()) <= 7:
        myLabel2 = Label(root, text='Hm, not bad, but not glad').grid(row=2, column=0)
    if 7 < int(clicked.get()) <= 10:
        myLabel2 = Label(root, text='Maan, that is GREAT!').grid(row=2, column=0)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


clicked = IntVar()
clicked.set(nums[0])
myLabel = Label(root, text='What is your mood?', font=10).grid(row=0, column=2)
op = OptionMenu(root, clicked, *nums).grid(row=0, column=3)
btn = Button(root, text='Show choice', command=show).grid(row=1, column=2, columnspan=3)

root.mainloop()
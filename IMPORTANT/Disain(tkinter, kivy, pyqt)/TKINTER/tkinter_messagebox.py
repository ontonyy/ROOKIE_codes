from tkinter import *
from tkinter import messagebox

# showinfo, showwarning, showerror, askquestion, askokcancel

root = Tk()


def popip():
    response = messagebox.askquestion('THIS IS MY POPIP', 'popip, popip?!')
    main = Label(root, text=response).pack()
    while True:
        if response == 'yes':
            response2 = messagebox.askquestion('sure?!', 'Are you sure?!')
            if response2 == 'no':
                break
        elif response == 'no':
            break

Button(root, text='POPIP', command=popip).pack()

root.mainloop()
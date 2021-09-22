from tkinter import *
import random
import string


root = Tk()
root.geometry("200x200")


password = Entry(root, text='password', show="*")
password.pack()
myLabel = Label(root, text="Enter a password: ").pack()
att = 0


def send():
    global att

    chars = string.ascii_letters + string.digits
    chars_list = list(chars)

    guess_password = ""

    while guess_password != str(password.get()):
        att += 1
        guess_password = random.choices(chars_list, k=len(str(password.get())))

        if guess_password == list(str(password.get())):
            print("Your password is: " + "".join(guess_password) + f", after {att} attempts")
            break


btn = Button(root, text='Click me!', command=send).pack()
root.mainloop()


input()

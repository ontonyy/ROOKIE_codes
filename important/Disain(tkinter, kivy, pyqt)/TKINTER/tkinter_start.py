from tkinter import *
from tkinter import messagebox


def btn_click():
    login = loginInput.get()
    password = passField.get()

    info_str = f'Данные: {str(login)}, {str(password)}'
    messagebox.showinfo(title='Ну ты и дурачок, девочка', message=f"Это фейк значок был, ищи другой\n{info_str}")


root = Tk()
root['bg'] = '#0928D3'
root.title('Basic')
root.wm_attributes('-alpha', 1)
root.geometry('600x600')

frame = Frame(root, bg='cyan')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title = Label(frame, text='Это секретное приложение', bg='cyan', font=50)
title2 = Label(root, text='Введите данные для входа', bg='orange', font=30)
title.pack()
title2.pack(pady=30)

loginInput = Entry(frame, bg='white', font=30)
loginInput.pack()

passField = Entry(frame, bg='white', font=30, show="*")
passField.pack()

btn = Button(frame, text='Вход', bg='yellow', command=btn_click, font=0)
btn.pack()

root.mainloop()
input()
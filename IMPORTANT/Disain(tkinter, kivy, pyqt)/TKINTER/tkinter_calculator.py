from tkinter import *

root = Tk()
root['bg'] = 'grey'

main = Entry(root, borderwidth=6, width=50)
main.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def num(number):
    global main
    current = main.get()
    main.delete(0, END)
    main.insert(0, str(current) + str(number))

def plus():
    global math, first_num
    f_num = main.get()
    math = 'plus'
    first_num = int(f_num)
    main.delete(0, END)

def minus():
    global math, first_num
    f_num = main.get()
    math = 'minus'
    first_num = int(f_num)
    main.delete(0, END)

def div():
    global math, first_num
    f_num = main.get()
    math = 'div'
    first_num = int(f_num)
    main.delete(0, END)

def mult():
    global math, first_num
    f_num = main.get()
    math = 'mult'
    first_num = int(f_num)
    main.delete(0, END)

def clear():
    global main
    main.delete(0, END)

def equal():
    second_num = main.get()
    main.delete(0, END)
    if math == 'plus':
        main.insert(0, first_num + int(second_num))
    elif math == 'minus':
        main.insert(0, first_num - int(second_num))
    elif math == 'mult':
        main.insert(0, first_num * int(second_num))
    elif math == 'div':
        main.insert(0, first_num / int(second_num))


btn1 = Button(root, text='1', padx=60, pady=30, command=lambda: num('1'), bg='black', fg='white', font=5)
btn2 = Button(root, text='2', padx=60, pady=30, command=lambda: num('2'), bg='black', fg='white', font=5)
btn3 = Button(root, text='3', padx=60, pady=30, command=lambda: num('3'), bg='black', fg='white', font=5)
btn4 = Button(root, text='4', padx=60, pady=30, command=lambda: num('4'), bg='black', fg='white', font=5)
btn5 = Button(root, text='5', padx=60, pady=30, command=lambda: num('5'), bg='black', fg='white', font=5)
btn6 = Button(root, text='6', padx=60, pady=30, command=lambda: num('6'), bg='black', fg='white', font=5)
btn7 = Button(root, text='7', padx=60, pady=30, command=lambda: num('7'), bg='black', fg='white', font=5)
btn8 = Button(root, text='8', padx=60, pady=30, command=lambda: num('8'), bg='black', fg='white', font=5)
btn9 = Button(root, text='9', padx=60, pady=30, command=lambda: num('9'), bg='black', fg='white', font=5)
btn0 = Button(root, text='0', padx=60, pady=30, command=lambda: num('0'), bg='black', fg='white', font=5)

btn_plus = Button(root, text='+', padx=60, pady=30, command=plus, bg='black', fg='white', font=0)
btn_minus = Button(root, text='-', padx=60, pady=30, command=minus, bg='black', fg='white', font=0)
btn_mult = Button(root, text='*', padx=60, pady=30, command=mult, bg='black', fg='white', font=0)
btn_div = Button(root, text='/', padx=60, pady=30, command=div, bg='black', fg='white', font=0)
btn_clear = Button(root, text='C', padx=60, pady=30, command=clear, bg='black', fg='white', font=0)
btn_equal = Button(root, text='=', padx=60, pady=30, command=equal, bg='black', fg='white', font=0)



btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)

btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)

btn0.grid(row=4, column=0)

btn_plus.grid(row=1, column=3)
btn_minus.grid(row=2, column=3)
btn_mult.grid(row=3, column=3)
btn_div.grid(row=4, column=3)
btn_clear.grid(row=4, column=2)
btn_equal.grid(row=4, column=1)

root.mainloop()

































# # Taking 1 number, delete it and taking second number, and then some action with these numbers
# from tkinter import *
#
# root = Tk()
# root.title('Simple Calculator')
# root['bg'] = 'grey'
#
# e = Entry(root, width=50, borderwidth=3)
# e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
#
#
# def button_click(number):
#     global e
#     current = e.get()
#     e.delete(0, END)
#     e.insert(0, str(current) + str(number))
#
#
# def button_clear():
#     e.delete(0, END)
#
#
# def add_button():
#     first_num = e.get()
#     global f_num
#     global math
#     math = "addition"
#     f_num = int(first_num)
#     e.delete(0, END)
#
#
# def button_equal():
#     second_num = e.get()
#     e.delete(0, END)
#     if math == 'addition':
#         e.insert(0, f_num + int(second_num))
#     elif math == 'subtract':
#         e.insert(0, f_num - int(second_num))
#     elif math == 'multiply':
#         e.insert(0, f_num * int(second_num))
#     elif math == 'division':
#         e.insert(0, f_num / int(second_num))
#
#
#
# def minus_button():
#     first_num = e.get()
#     global f_num
#     global math
#     math = "subtract"
#     f_num = int(first_num)
#     e.delete(0, END)
#
#
# def mult_button():
#     first_num = e.get()
#     global f_num
#     global math
#     math = "multiply"
#     f_num = int(first_num)
#     e.delete(0, END)
#
#
# def div_button():
#     first_num = e.get()
#     global f_num
#     global math
#     math = "division"
#     f_num = int(first_num)
#     e.delete(0, END)
#
#
# button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click('1'), bg='black', fg='white')
# button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click('2'), bg='black', fg='white')
# button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click('3'), bg='black', fg='white')
# button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click('4'), bg='black', fg='white')
# button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click('5'), bg='black', fg='white')
# button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click('6'), bg='black', fg='white')
# button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click('7'), bg='black', fg='white')
# button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click('8'), bg='black', fg='white')
# button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click('9'), bg='black', fg='white')
# button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click('0'), bg='black', fg='white')
#
# button_clear = Button(root, text='clear', padx=78, pady=20, command=button_clear, bg='black', fg='white')
# button_add = Button(root, text='+', padx=40, pady=20, command=add_button, bg='black', fg='white')
# button_minus = Button(root, text='-', padx=40, pady=20, command=minus_button, bg='black', fg='white')
# button_mult = Button(root, text='*', padx=40, pady=20, command=mult_button, bg='black', fg='white')
# button_div = Button(root, text='/', padx=40, pady=20, command=div_button, bg='black', fg='white')
# button_equal = Button(root, text='=', padx=86, pady=20, command=button_equal, bg='black', fg='white')
#
# button_9.grid(row=1, column=2)
# button_8.grid(row=1, column=1)
# button_7.grid(row=1, column=0)
#
# button_6.grid(row=2, column=2)
# button_5.grid(row=2, column=1)
# button_4.grid(row=2, column=0)
#
# button_3.grid(row=3, column=2)
# button_2.grid(row=3, column=1)
# button_1.grid(row=3, column=0)
# button_0.grid(row=4, column=0)
#
# button_add.grid(row=1, column=3)
# button_minus.grid(row=2, column=3)
# button_mult.grid(row=3, column=3)
# button_div.grid(row=4, column=3)
# button_clear.grid(row=4, column=1, columnspan=2)
# button_equal.grid(row=5, column=1, columnspan=2)
#
# root.mainloop()
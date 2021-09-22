from tkinter import *

root = Tk()
root.title('Radio Buttons')

MODES = [
    ('Volvo', 'Volvo'),
    ('Nissan', 'Nissan'),
    ('Mazda', 'Mazda'),
    ('Hyundai', 'Hyundai')
]

car = StringVar()
car.set('Volvo')

for text, mode in MODES:
    Radiobutton(root, text=text, variable=car, value=mode).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


myButton = Button(root, text='Click me!', command=lambda: clicked(car.get()))
myButton.pack()

mainloop()
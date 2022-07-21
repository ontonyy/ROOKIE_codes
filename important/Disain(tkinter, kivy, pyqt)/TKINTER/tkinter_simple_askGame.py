from tkinter import *

root = Tk()
root['bg'] = 'cyan'
# root.geometry('500x500')
root.title('BLITZ GAME')

score = 0
attempts = 0
year = StringVar()
year.set('1941')

myLabel1 = Label(root, text='1) When started the Second War?', bg='black', fg='white').pack(anchor=W)
answers = [
    ('1941', '1941'),
    ('1939', '1939'),
    ('1945', '1945')
]

for text, mode in answers:
    Radiobutton(root, text=text, value=mode, variable=year).pack(anchor=W)


def clicked(value):
    global attempts, score
    if value == '1941':
        Label(root, text='Mõtle veel kord, answer is not correct!').pack(anchor=W)
        attempts += 1

    if value == '1945':
        Label(root, text='Mõtle veel kord, answer is not correct!').pack(anchor=W)
        attempts += 1

    if value == '1939':
        myLabel2 = Label(root, text='THIS IS CORRECT ANSWER!')
        myLabel2.pack(anchor=W)
        attempts += 1
        score += 1

        car = StringVar()
        car.set('Volvo')

        myLabel3 = Label(root, text='2) Which mark of cars was made in Germany?', bg='black', fg='white')
        myLabel3.pack(anchor=W)
        cars = [
            ('Volvo', 'Volvo'),
            ('Nissan', 'Nissan'),
            ('BMW', 'BMW')
        ]

        for text, mode in cars:
            Radiobutton(root, text=text, value=mode, variable=car).pack(anchor=W)

        btn = Button(root, text='ANSWER', command=lambda: clicked2(car.get()))
        btn.pack()


def clicked2(value1):
    global attempts, score
    if value1 == 'Volvo':
        Label(root, text='Mõtle veel kord, да не правильный это ответ!').pack(anchor=W)
        attempts += 1

    if value1 == 'Nissan':
        Label(root, text='Mõtle veel kord, да не правильный это ответ!').pack(anchor=W)
        attempts += 1

    if value1 == 'BMW':
        myLabel2 = Label(root, text='THIS IS CORRECT ANSWER!')
        myLabel2.pack(anchor=W)
        attempts += 1
        score += 1

        club = StringVar()
        club.set('Manchester City')

        myLabel3 = Label(root, text='3) Who is won UEFA Champions League in 2020/21?', bg='black', fg='white')
        myLabel3.pack(anchor=W)
        clubs = [
            ('Manchester City', 'Manchester City'),
            ('FC Barcelona', 'FC Barcelona'),
            ('Chelsea', 'Chelsea')
        ]

        for text, mode in clubs:
            Radiobutton(root, text=text, value=mode, variable=club).pack(anchor=W)

        btn = Button(root, text='ANSWER', command=lambda: clicked3(club.get()))
        btn.pack()


def clicked3(value2):
    global attempts, score
    if value2 == 'Manchester City':
        Label(root, text='Mõtle veel kord, да не правильный это ответ!').pack(anchor=W)
        attempts += 1

    if value2 == 'FC Barcelona':
        Label(root, text='Mõtle veel kord, да не правильный это ответ!').pack(anchor=W)
        attempts += 1

    if value2 == 'Chelsea':
        myLabel2 = Label(root, text='THIS IS CORRECT ANSWER!')
        myLabel2.pack(anchor=W)
        attempts += 1
        score += 1
        Label(root, text=f'YOU HAVE {attempts} attempts and of course {score} correct answers', bg='blue', fg='white').pack()


btn = Button(root, text='ANSWER', command=lambda: clicked(year.get()))
btn.pack()

mainloop()

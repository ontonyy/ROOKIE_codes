from tkinter import *
import requests
from bs4 import BeautifulSoup
from PIL import ImageTk, Image

root = Tk()
root['bg'] = 'cyan'
root.title('EURO 2020')

r = requests.get('https://www.euro-football.ru/category/result/1003096931')

soup = BeautifulSoup(r.text)

score = soup.find_all('div', class_='calendar-item__match')     # Счёт матча
times = soup.find_all('div', class_='calendar-item__time')      # Время матча
calendar = soup.find_all('div', class_='calendar__list')    # Полная информация о матче
days = soup.find_all('span', class_='calendar-list__day')

scores = []
daiz = []
timez = []
for s in score:
    s_strip = s.text.strip('\n').replace('\n', ' ')
    scores.append(s_strip.replace(' ', '   '))

for day in days:
    daiz.append(day.text)

for time in times:
    timez.append(time.text)


def match12():
    top = Toplevel()
    top.title('12 JUNE - EURO 2021')
    top['bg'] = 'cyan'
    for x, y in zip(scores[12:15], timez[12:15]):
        info = Label(top, text='\nDAY MATCH --> ' + daiz[4] + " || " + y + '\n\n' + x, bg='#fbb040')
        info.grid(padx=10, pady=10)
    btn = Button(top, text='Close info', command=top.destroy).grid()


def match13():
    top = Toplevel()
    top.title('13 JUNE - EURO 2021')
    top['bg'] = 'cyan'
    for x, y in zip(scores[9:12], timez[9:12]):
        info = Label(top, text='\nDAY MATCH --> ' + daiz[3] + " || " + y + '\n\n' + x, bg='#fbb040')
        info.grid(padx=10, pady=10)
    btn = Button(top, text='Close info', command=top.destroy).grid()


def match14():
    top = Toplevel()
    top.title('14 JUNE - EURO 2021')
    top['bg'] = 'cyan'
    for x, y in zip(scores[6:9], timez[6:9]):
        info = Label(top, text='\nDAY MATCH --> ' + daiz[2] + " || " + y + '\n\n' + x, bg='#fbb040')
        info.grid(padx=10, pady=10)
    btn = Button(top, text='Close info', command=top.destroy).grid()


def match15():
    top = Toplevel()
    top.title('15 JUNE - EURO 2021')
    top['bg'] = 'cyan'
    for x, y in zip(scores[3:6], timez[3:6]):
        info = Label(top, text='\nDAY MATCH --> ' + daiz[1] + " || " + y + '\n\n' + x, bg='#fbb040')
        info.grid(padx=10, pady=10)
    btn = Button(top, text='Close info', command=top.destroy).grid()


def match16():
    top = Toplevel()
    top.title('16 JUNE - EURO 2021')
    top['bg'] = 'cyan'
    for x, y in zip(scores[:3], timez[:3]):
        info = Label(top, text='\nDAY MATCH --> ' + daiz[0] + " || " + y + '\n\n' + x, bg='#fbb040')
        info.grid(padx=10, pady=10)
    btn = Button(top, text='Close info', command=top.destroy).grid()


main = Label(root, text='EURO 2020 - DAYS', bg='blue', fg='white', font=20, borderwidth=3, padx=40).grid(row=0, column=2, columnspan=2)

btn12 = Button(root, text='12 июня матчи', command=match12, borderwidth=3, bg='blue', fg='white').grid(row=1, column=1)
btn13 = Button(root, text='13 июня матчи', command=match13, borderwidth=3, bg='blue', fg='white').grid(row=1, column=4)
btn14 = Button(root, text='14 июня матчи', command=match14, borderwidth=3, bg='blue', fg='white').grid(row=2, column=1)
btn15 = Button(root, text='15 июня матчи', command=match15, borderwidth=3, bg='blue', fg='white').grid(row=2, column=4)
btn16 = Button(root, text='16 июня матчи', command=match16, borderwidth=3, bg='blue', fg='white').grid(row=3, column=1)


root.mainloop()

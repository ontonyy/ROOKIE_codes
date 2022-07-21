from tkinter import *
import pyowm
from pyowm import OWM

root = Tk()
root.title("Weather")
root.geometry('500x500')
root['bg'] = 'grey'


def weather():
    city = we.get()

    # 2 способа получить информацию о погоде, 2 разных модуля

    owm = pyowm.OWM('ed0a984565c3a3c57c62dec43a395b4d')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    w = observation.weather

    temp = w.temperature('celsius')['temp']
    wi = w.wind()['speed']
    st = w.detailed_status

    info['text'] = (f'{str(city)} {temp}℃!'
                    f'\n{str(city)} {wi} м/с'
                    f'\nstatus - {st}')
   
    if temp <= 0:
        info['bg'] = 'blue'
    if 0 < temp <= 10:
        info['bg'] = 'green'
    if 10 < temp <= 20:
        info['bg'] = 'yellow'
    if 20 < temp <= 30:
        info['bg'] = 'orange'

    # Погода с распаковкой словаря, с модулем pyowm как по мне легче
    # key = 'ed0a984565c3a3c57c62dec43a395b4d'
    #
    # url = 'http://api.openweathermap.org/data/2.5/weather'
    #
    # params = {'APPID': key, 'q': city, 'units': 'metric'}
    #
    # result = requests.get(url, params=params)
    #
    # weather = result.json()
    #
    # info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]} ℃!' \
    #                f'\n{str(weather["name"])}: {weather["wind"]["speed"]} м/с'


we = Entry(root, width=30, bd=3)
we.pack(pady=10)
btn = Button(root, text="Show Weather!", command=weather, bd=5, width=20)
btn.pack()
f = Frame(root, bg='black')
f.place(relx=0.14, rely=0.2, relwidth=0.7, relheight=0.8)
info = Label(f, text='Погодная информация', bg='white', fg='black', font=20)
info.pack(pady=150)
root.mainloop()

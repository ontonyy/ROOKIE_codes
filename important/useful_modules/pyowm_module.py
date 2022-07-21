from pyowm.utils.config import get_default_config
import pyowm

city = input("Какой город Вас интересует?: ")

owm = pyowm.OWM('ed0a984565c3a3c57c62dec43a395b4d')
mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)
w = observation.weather
config_dict = get_default_config()
config_dict['language'] = 'ru'
# Температура
temperature = w.temperature('celsius')['temp']

#Скорость ветра
wi = w.wind()['speed']

# Статус города
st = w.detailed_status

print(f"\nВ городе {city}, сейчас температура: {temperature} по Цельсию!"
      f"\nСкорость ветра в {city} - {wi} м/с."
      f"\nСтатус города - {st}.\n")

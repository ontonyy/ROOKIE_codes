import telebot
from pyowm import OWM
import pyowm

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bear_photo = open(
            'projects\IMPORTANT/telegram_bots/telegram_stickers_pics/bear.jpg',
            'rb')
        bot.send_photo(message.chat.id, bear_photo)
        bot.send_message(message.chat.id, 'Welcome, {0.first_name}.\
            \nWith me you can know the weather in different countries\
            \nJust write a country: '                                                                                                                                                                                         .format(message.from_user))

    @bot.message_handler(content_types=['text'])
    def weather_check(message):
        try:
            owm = pyowm.OWM('ed0a984565c3a3c57c62dec43a395b4d')
            mgr = owm.weather_manager()
            observation = mgr.weather_at_place(message.text)
            w = observation.weather

            temp = w.temperature('celsius')['temp']
            wi = w.wind()['speed']
            status = w.detailed_status
            weather_message = f'{message.text} - {temp}℃!\
                \nWind: {wi} m/s\
                \nStatus: {status}'

            bot.send_message(message.chat.id, weather_message)

            if int(temp) < 10:
                cold_photo = open(
                    'projects\IMPORTANT/telegram_bots/telegram_stickers_pics\cold_photo.webp', 'rb')
                bot.send_sticker(message.chat.id, cold_photo)

            if 10 < int(temp) < 20:
                medium_photo = open(
                    'projects\IMPORTANT/telegram_bots/telegram_stickers_pics\medium_photo.webp', 'rb')
                bot.send_sticker(message.chat.id, medium_photo)
            if int(temp) > 20:
                hot_photo = open(
                    'projects\IMPORTANT/telegram_bots/telegram_stickers_pics\hot_photo.webp', 'rb')
                bot.send_sticker(message.chat.id, hot_photo)
        except:
            bot.send_message(message.chat.id, 'I do not have any response!!!')
    bot.polling(none_stop=True, interval=0)

if __name__ == '__main__':
    telegram_bot('1811866101:AAF2PBUArIc1to2XVzsXXURcE6IHiWsgJo8')

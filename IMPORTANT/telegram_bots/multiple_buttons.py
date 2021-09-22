import random
from telebot import types
import telebot
from datetime import datetime
import pyowm
from pyowm import OWM
from selenium import webdriver
import pickle
import time


def telegram_bot(token):
    bot = telebot.TeleBot(token)
    print('Bot start working')

    @bot.message_handler(commands=['start'])
    def start_message(message):
        sticker = open(
            'projects\IMPORTANT/telegram_bots/telegram_stickers_pics\lord_hello.webp',
            'rb')
        bot.send_sticker(message.chat.id, sticker)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('🎱 Random number')
        item2 = types.KeyboardButton('💰 Crypto coins')
        item3 = types.KeyboardButton('🌦 Weather')
        item4 = types.KeyboardButton('🔮 Another')
        markup.add(item1, item2, item3, item4)

        bot.send_message(message.chat.id,
                         'Welcome, {0.first_name}!\
                                            \nI am bot, which can everything, but...\
                                            \nMy owner is jusTony'.format(message.from_user),
                         reply_markup=markup)

    @bot.message_handler(content_types=['text'])
    def send_message(message):
        options = webdriver.ChromeOptions()
        options.headless = True

        driver = webdriver.Chrome(
            r'C:\ROOKIE_codes\projects\IMPORTANT\useful_modules\selenium_module\chromedriver.exe',
            options=options)

        if message.chat.type == 'private':
            if message.text == '🎱 Random number':
                bot.send_message(
                    message.chat.id,
                    '- - - > ' + str(random.randint(0, 100)) + ' < - - -')

            elif message.text == '💰 Crypto coins':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Bitcoin')
                item2 = types.KeyboardButton('Ethereum')
                item3 = types.KeyboardButton('Binancecoin')
                item4 = types.KeyboardButton('Top 10 coins')
                item5 = types.KeyboardButton('⬅️ back')
                markup.add(item1, item2, item3, item4, item5)
                bot.send_message(message.chat.id,
                                 'About crypto, hm okay!',
                                 reply_markup=markup)

            elif message.text == 'Bitcoin':
                bot.send_message(message.chat.id, 'Wait 10 seconds ^_^')

                driver.get('https://www.worldcoinindex.com/')
                for cookie in pickle.load(
                        open(
                            r'C:\ROOKIE_codes\projects\IMPORTANT\telegram_bots\cookie\session',
                            'rb')):
                    driver.add_cookie(cookie)

                driver.refresh()
                time.sleep(2)

                prices = driver.find_elements_by_class_name('lastprice')
                names = driver.find_elements_by_class_name('bitcoinName')
                percents = driver.find_elements_by_class_name('percentage')
                text = []
                for n, c, p in zip(names[1:], prices[1:], percents):
                    try:
                        text.append(
                            f'{n.text} - {c.text[2:]} euro. Percent: {p.text}')
                    except:
                        continue

                for name in text:
                    if 'Bitcoin' in name:
                        bot.send_message(
                            message.chat.id,
                            f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\n{name}")

            elif message.text == 'Ethereum':
                bot.send_message(message.chat.id, 'Wait 10 seconds ^_^')

                driver.get('https://www.worldcoinindex.com/')

                for cookie in pickle.load(
                        open(
                            r'C:\ROOKIE_codes\projects\IMPORTANT\telegram_bots\cookie\session',
                            'rb')):
                    driver.add_cookie(cookie)

                driver.refresh()
                time.sleep(2)

                prices = driver.find_elements_by_class_name('lastprice')
                names = driver.find_elements_by_class_name('bitcoinName')
                percents = driver.find_elements_by_class_name('percentage')
                text = []
                for n, c, p in zip(names[1:], prices[1:], percents):
                    try:
                        text.append(
                            f'{n.text} - {c.text[2:]} euro. Percent: {p.text}')
                    except:
                        continue

                for name in text:
                    if 'Ethereum' in name:
                        bot.send_message(
                            message.chat.id,
                            f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\n{name}")

            elif message.text == 'Binancecoin':
                bot.send_message(message.chat.id, 'Wait 10 seconds ^_^')

                driver.get('https://www.worldcoinindex.com/')
                for cookie in pickle.load(
                        open(
                            r'C:\ROOKIE_codes\projects\IMPORTANT\telegram_bots\cookie\session',
                            'rb')):
                    driver.add_cookie(cookie)

                driver.refresh()
                time.sleep(2)

                prices = driver.find_elements_by_class_name('lastprice')
                names = driver.find_elements_by_class_name('bitcoinName')
                percents = driver.find_elements_by_class_name('percentage')
                text = []
                for n, c, p in zip(names[1:], prices[1:], percents):
                    try:
                        text.append(
                            f'{n.text} - {c.text[2:]} euro. Percent: {p.text}')
                    except:
                        continue

                for name in text:
                    if 'Binancecoin' in name:
                        bot.send_message(
                            message.chat.id,
                            f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\n{name}"
                        )
                    else:
                        continue

            elif message.text == 'Top 10 coins':
                bot.send_message(message.chat.id, 'Wait 10 seconds ^_^')

                driver.get('https://www.worldcoinindex.com/')
                for cookie in pickle.load(
                        open(
                            r'C:\ROOKIE_codes\projects\IMPORTANT\telegram_bots\cookie\session',
                            'rb')):
                    driver.add_cookie(cookie)

                driver.refresh()
                time.sleep(2)

                prices = driver.find_elements_by_class_name('lastprice')
                names = driver.find_elements_by_class_name('bitcoinName')
                percents = driver.find_elements_by_class_name('percentage')
                text = []
                for n, c, p, num in zip(names[1:], prices[1:], percents,
                                        range(1, 11)):
                    try:
                        text.append(
                            f'{num}) {n.text} - {c.text[2:]} euro. Percent: {p.text}'
                        )
                    except:
                        continue
                top10 = '\n\n'.join(text[:11])
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\n{top10}")

            elif message.text == '🔮 Another':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('☯️ About author')
                item2 = types.KeyboardButton('⛔️ Black box')
                item3 = types.KeyboardButton('🤖 Bot mood')
                item4 = types.KeyboardButton('⬅️ back')
                markup.add(item1, item2, item3, item4)
                bot.send_message(message.chat.id,
                                 'Another functions',
                                 reply_markup=markup)

            elif message.text == '☯️ About author':
                bot.send_message(
                    message.chat.id, 'Author is Anton Gavrilin\
                                                \nRookie in IT field\
                                                \nIn future you will hear more\
                                                \n| o | n | t | o | n | y |\
                                                \nV    V    V    V    V    V   V'
                )
                photo = open(
                    r'projects\IMPORTANT\telegram_bots\telegram_stickers_pics\bot_master.jpg',
                    'rb')
                bot.send_photo(message.chat.id, photo)

            elif message.text == '⛔️ Black box':
                for _ in range(6):
                    sticker = open(
                    r'projects\IMPORTANT\telegram_bots\telegram_stickers_pics\hacker.webp',
                    'rb')
                    bot.send_sticker(message.chat.id, sticker)
                    bot.send_message(
                        message.chat.id,
                        'DUDOS IS STARTING\nHEHEheheheHEhehHEheHE')


            elif message.text == '⬅️ back':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('🎱 Random number')
                item2 = types.KeyboardButton('💰 Crypto coins')
                item3 = types.KeyboardButton('🌦 Weather')
                item4 = types.KeyboardButton('🔮 Another')
                markup.add(item1, item2, item3, item4)

                bot.send_message(message.chat.id,
                                 'Okay I\'m going back, sorry...',
                                 reply_markup=markup)

            elif message.text == '🤖 Bot mood':
                markup = types.InlineKeyboardMarkup(row_width=2)
                mood1 = types.InlineKeyboardButton('All is good',
                                                   callback_data='good')
                mood2 = types.InlineKeyboardButton('Bad, bad, bad...',
                                                   callback_data='bad')
                markup.add(mood1, mood2)

                bot.send_message(
                    message.chat.id,
                    'I am fine, AND I AM BOT.\nNow how are you bot :) ?',
                    reply_markup=markup)

            elif message.text == '🌦 Weather':
                bot.send_message(message.chat.id, 'Write some city: ')
                bot.register_next_step_handler(message, weather_check)

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

            if int(temp) <= 10:
                cold_photo = open(
                    'projects\IMPORTANT/telegram_bots/telegram_stickers_pics\cold_photo.webp',
                    'rb')
                bot.send_sticker(message.chat.id, cold_photo)

            if 10 < int(temp) <= 20:
                medium_photo = open(
                    'projects\IMPORTANT/telegram_bots/telegram_stickers_pics\medium_photo.webp',
                    'rb')
                bot.send_sticker(message.chat.id, medium_photo)
            if int(temp) > 20:
                hot_photo = open(
                    'projects\IMPORTANT/telegram_bots/telegram_stickers_pics\hot_photo.webp',
                    'rb')
                bot.send_sticker(message.chat.id, hot_photo)
        except:
            bot.send_message(message.chat.id, 'I do not have any response!!!')

    @bot.callback_query_handler(func=lambda call: True)
    def callback_check(call):
        try:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'THAS A REALLY GOOD')
                bot.answer_callback_query(callback_query_id=call.id,
                                          show_alert=True,
                                          text='I\'m glad, go fuck your mouth')

            elif call.data == 'bad':
                bot.send_message(call.message.chat.id,
                                 'I do not know what I can do:(')
                bot.answer_callback_query(
                    callback_query_id=call.id,
                    show_alert=True,
                    text='GO to drink something\nOf course TEA')

        except:
            bot.send_message(call.message.chat.id,
                             'I do not have any response')

    bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':
    telegram_bot('1853778580:AAHmtl4zeRZ3-Yc2na6hxucukONNSjd3DGg')
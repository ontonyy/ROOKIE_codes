import requests
from bs4 import BeautifulSoup
from datetime import datetime
import telebot
import random

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        # Send sticker and message in start
        sticker = open(
            'projects\IMPORTANT/telegram_bots/telegram_stickers_pics\dog_welcome.webp',
            'rb')
        bot.send_sticker(message.chat.id, sticker)

        bot.send_message(message.chat.id, "Hello {0.first_name}, write 'price', to know Bitcoin price!".format(message.from_user))

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        # Sending a BItcoin price
        if message.text.lower() == 'price':
            try:
                r = requests.get('https://coinmarketcap.com/')
                soup = BeautifulSoup(r.text, 'lxml')
                bitcoin = soup.find('div', class_='sc-131di3y-0').find('a',
                                                           class_='cmc-link')
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nBitcoin price: {bitcoin.text}")

            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id,
                                 'Damn...Something was wrong!')
        else:
            messages = [
                'No, no, no, you should write "price"',
                'Check the rules, AND WRITE RIGHT THING',
                'Whaaat check a command!'
            ]
            bot.send_message(message.chat.id, random.choice(messages))

    bot.polling()

if __name__ == '__main__':
    telegram_bot('1816810335:AAF_C1pzlW9kd_IdR9UUN6TrTkmGxnhF2wo')
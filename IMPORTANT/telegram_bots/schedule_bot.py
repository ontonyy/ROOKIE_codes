import telebot
from datetime import datetime
import schedule
import time
from threading import Thread

users = []

time_now = datetime.now()

def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(1)


def telegram_bot(token):

    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def alert_message(message):
        print(time_now.hour)
        bot.send_message(message.chat.id, 'WAKE UP HORNY!')
        users.append(message.chat.id)

    def SPAM():
        for u in users:
            bot.send_message(u, 'SPAM <> SPAM')

    schedule.every().second.do(SPAM)
    Thread(target=schedule_checker).start()

    bot.polling(none_stop=True, interval=0)

if __name__ == '__main__':
    telegram_bot('1827948343:AAEHjmymhU_h0GjMV6YMPWiebzpnvER2vGA')

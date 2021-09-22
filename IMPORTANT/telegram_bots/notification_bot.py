from telebot import types, TeleBot
from selenium import webdriver
from datetime import datetime
import time
import pickle
import schedule
from threading import Thread

users = []


def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(1)


def telegram_bot(token):
    options = webdriver.ChromeOptions()
    options.headless = True

    driver = webdriver.Chrome(
        r'C:\ROOKIE_codes\projects\IMPORTANT\useful_modules\selenium_module\chromedriver.exe',
        options=options)

    bot = TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'Hello, Dear!')
        users.append(message.chat.id)

    def check_coin():
        driver.get('https://www.worldcoinindex.com/')
        for cookie in pickle.load(
                open(
                    r'C:\ROOKIE_codes\projects\IMPORTANT\telegram_bots\cookie\session',
                    'rb')):
            driver.add_cookie(cookie)

        print('All is good!')

        driver.refresh()
        time.sleep(2)

        prices = driver.find_elements_by_class_name('lastprice')
        names = driver.find_elements_by_class_name('bitcoinName')
        percents = driver.find_elements_by_class_name('percentage')
        text = []
        price_bitcoin = []
        price_ethereum = []
        popul_coin = []
        name_text = []
        for n, c, p in zip(names[1:], prices[1:], percents):
            try:
                text.append(f'{n.text} - {c.text[2:]} euro. Percent: {p.text}')
                name_text.append(n.text)

                if 'Bitcoin' in n.text:
                    price_bitcoin.append(c.text[2:].replace(',', ''))

                if 'Ethereum' in n.text:
                    price_ethereum.append(c.text[2:].replace(',', ''))
            except:
                continue

        print("Coins is found")

        for name in name_text:
            if 'Bitcoin' == name and int(price_bitcoin[0]) >= 26000:
                for u in users:
                    bot.send_message(
                        u,
                        f"!!BITCOIN PRICE NOW!!\n-----> {price_bitcoin[0]} EURO <-----")
            if 'Ethereum' == name and int(price_ethereum[0].split('.')[0]) >= 1500:
                for u in users:
                    bot.send_message(
                        u,
                        f"!!ETHEREUM PRICE NOW!!\n-----> {price_ethereum[0].split('.')[0]} EURO <-----")
            else:
                continue

    schedule.every().minute.do(check_coin)
    Thread(target=schedule_checker).start()

    bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':
    telegram_bot('1827948343:AAEHjmymhU_h0GjMV6YMPWiebzpnvER2vGA')

import requests
from bs4 import BeautifulSoup
import telebot
from datetime import datetime

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        sticker = open(r'c:\ALL_CODES\python_projects\IMPORTANT\telegram_bots\telegram_stickers_pics\dog_welcome.webp', 'rb')
        bot.send_sticker(message.chat.id, sticker)
        bot.send_message(message.chat.id, "Welcome, {0.first_name}^_^\nType 'price' and you will see universe!".format(message.from_user))


    @bot.message_handler(content_types=['text'])
    def send_message(message):
        if message.text.lower() == "price":
            try:
                url = "https://coinmarketcap.com/"
                headers = {
                    "user-agent":
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 OPR/78.0.4093.184"
                }
                result = requests.get(url, headers=headers).text
                soup = BeautifulSoup(result, "lxml")
                print('Start working...')

                tbody = soup.find("tbody")
                coins = tbody.find_all("tr")

                for coin in coins[:10]:
                    name = coin.find(class_="cmc-link").get("href").replace(
                        "/currencies/", "")[:-1]
                    price = coin.find(class_="sc-131di3y-0 cLgOOr").text
                    bot.send_message(message.chat.id, f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}]\n{name} --> {price[1:]}$")
            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Daaaamn...Something was wrong")
        else:
            bot.send_message(message.chat.id, 'maaaan, check the rules!')
    bot.polling()

if __name__ == '__main__':
    telegram_bot('1982816190:AAGI5yRYRH0JA2fmcXja39PgvPvS95amBE8')
from selenium import webdriver
from telebot import *
from selenium import *
from selenium.webdriver.common.keys import Keys


def telegram_bot(TOKEN):
    bot = TeleBot(TOKEN)

    @bot.message_handler(commands=['start'])
    def bot_start(message):
        bot.send_message(
            message.chat.id,
            'Hello, dude <{0.first_name}>!\nThis bot send place screenshot\nJust write some place/address:'
            .format(message.from_user))

    @bot.message_handler(content_types=['text'])
    def message_send(message):
        bot.send_message(message.chat.id , 'Wait 15 seconds!')
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(
            executable_path=
            r'C:\ROOKIE_codes\projects\IMPORTANT\useful_modules\selenium_module\chromedriver.exe',
            options=options)

        driver.get('https://www.google.ru/maps/')
        time.sleep(2)

        driver.find_element_by_xpath(
            '/html/body/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button/span'
        ).click()
        time.sleep(2)

        input_place = driver.find_element_by_xpath(
            '/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/form/div/div[3]/div/input[1]'
        )
        input_place.send_keys(message.text + Keys.ENTER)
        time.sleep(2)

        driver.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[8]/div/div[3]/button').click()
        time.sleep(3)
        screen = str(message.text) + '.png'
        driver.save_screenshot(screen)

        message_user = message.text.replace(' ', '+')
        screen_send = open(screen, 'rb')
        bot.send_photo(message.chat.id, screen_send)
        bot.send_message(
            message.chat.id,
            f'Here is URL:\n\nhttps://www.google.ru/maps/search/{message_user}')

    bot.infinity_polling()


if __name__ == '__main__':
    telegram_bot('1894291407:AAHzulfmC9vGB-P6_-6EdJSFEsKNz35rA50')
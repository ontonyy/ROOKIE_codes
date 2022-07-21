import asyncio

import telepot
from telepot.exception import TelegramError
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle, \
    InputTextMessageContent, ReplyKeyboardMarkup, KeyboardButton
from telepot.loop import MessageLoop
from googletrans import Translator, constants

# Weird library for telegram bot creating, because of small documentation and info in Internet

super_token = "5519492104:AAHqshbIG-CmFdl6UDLSRqJWi4XtLvriaCw"


def get_token():
    print("[Connect] Enabling, need a token!")
    return input("Enter token: ")


class TelegramBot:
    def __init__(self):
        self.bot = None
        self.name = ""
        self.language = ""
        self.translate_bool = False

    def translate(self, text):
        trans = Translator().translate(text, dest=self.language)
        return trans.text

    def connect(self):
        try:
            # token = get_token()
            self.bot = telepot.Bot(super_token)
            self.name = self.bot.getMe().get("first_name")
        except TelegramError:
            print("\n[Error] Invalid token!")
            self.connect()

    def start(self):
        self.bot.message_loop({
            "chat": self.handle,
            "callback_query": self.on_callback_query
        })

        print(f"\n[{self.name}] Successfully start working...")

        while True:
            pass

    def handle(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(chat_id)
        message = msg["text"]
        markup = None

        bot_response = message

        if message == "/start":
            markup = ReplyKeyboardMarkup(keyboard=[
                ["Translator", "Anekdoter"]])  # all actions of bot
        elif message == "Translator":
            markup = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Russian", callback_data="ru"),
                 InlineKeyboardButton(text="German", callback_data="de")],
                [InlineKeyboardButton(text="English", callback_data="en"),
                 InlineKeyboardButton(text="Estonian", callback_data="et")],
                [InlineKeyboardButton(text="Chinese", callback_data="zh-cn"),
                 InlineKeyboardButton(text="Polish", callback_data="pl")]
            ])
            bot_response = "Choose a language: "
            self.translate_bool = True
        elif self.language != "" and self.translate_bool:
            bot_response = self.translate(message)
            self.language = ""
            self.translate_bool = False

        self.bot.sendMessage(chat_id, bot_response, reply_markup=markup)

    def on_callback_query(self, msg):
        query_id, from_id, query_data = telepot.glance(msg, flavor="callback_query")
        lang = constants.LANGUAGES[query_data]

        callback_message = "Something went wrong!"
        if lang:
            self.language = query_data
            print("Choosed language: ", lang)
            callback_message = "Understandable!"

        self.bot.answerCallbackQuery(query_id, callback_message)


if __name__ == '__main__':

    bot = TelegramBot()

    bot.connect()

    loop = asyncio.get_event_loop()
    loop.create_task(bot.start())

    loop.run_forever()
    bot.start()

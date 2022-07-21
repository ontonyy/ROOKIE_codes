import codecs
import os

import pytz
import random
import time

from deep_translator import GoogleTranslator, PonsTranslator
from deep_translator.exceptions import LanguageNotSupportedException

# own scripts
from currency_exchange import *
from other_files.constants import *
from inline import *
from password_manager import PasswordManager
from que_teleg import QueBot
from small_scripts import *

print("| BOT | - start working...")

keyboards_buttons = ["Random number", "Throw dice", "Random person", "Random image"]
random_person_image = "https://thispersondoesnotexist.com/image"
random_image = "https://picsum.photos/1200"

additional_que = QueBot(
    ["Go", "Python", "Java", "C++", "JavaScript", "Fortran"],
    "Please choose your programming languages: ",
    "Chosen programming languages")

pm = PasswordManager()

password_init_text = """Write in format:
        *site* = *password* (Add password)
        get *site* (Get password)
        get (Get all passwords)
        delete *site* (Delete password)
        delete (Delete all passwords)
        q (Quit)"""

translate_init_text = """Write in format:
        *source* to *destination*"""

currency_init_text = """Write in format:
        *currency* to *currency* : *amount*
        *currency* to *currency* in *year* : *amount*"""

notify_init_text = """Write in format:
        *week day* **:** - time when notify
        *amount* minute - every amount minute notify
        *amount* second - every amount second notify
        *amount* hour - every amount hour notify
        quit - Quit from notifier
        stop - stop all alerts"""

start_init_text = "Let's go do something, choose a command, ma friend\n" \
                  "😶‍🌫️🤯🤩😎👺👾🤖💪🤙👀👮‍♂️🐲🌚🌝🦍🐊🐅"

# Commands:
# /start_buttons - Start another commands only like buttons
# /echo - Simple echo playing
# /que - Random questionnaire
# /anekdot - Random anekdot(joke) from "Ебутся как-то 4 клоуна" group
# /translate - Translate text or word
# /currency_exchange - Actions with currencies
# /passwords - Handle passwords (encrypt and hold)
# /notifier - Notify in special time or every period of time


class TelegramBot:
    def __init__(self):
        self.echo_run = False
        self.trans = False
        self.check_random = False
        self.currency = False
        self.password = False
        self.notify = False
        self.notify_message = ""
        self.languages = tuple()
        self.print_text = ""
        self.likes = self.dislikes = 0
        self.markup = None
        self.count_pass = 0
        self.update = self.context = None

    async def echo(self, update, context):
        self.echo_run = not self.echo_run
        await update.message.reply_text(update.message.text)

    async def start_buttons(self, update, context) -> None:
        buttons = [
            [KeyboardButton("Random number"), KeyboardButton("Throw dice")],
            [KeyboardButton("Random person"), KeyboardButton("Random image")],
        ]
        await update.message.reply_text(text="Start, you can click to buttons",
                                        reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))

    async def get_anekdot(self, update, context):
        with codecs.open("other_files/anekdots.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            anekdot = random.choice(lines)
        print(f"[Anekdot] {update.effective_user.username} get a random anekdot")
        await update.message.reply_text(anekdot)

    async def translate(self, update, context):
        self.trans = True
        await update.message.reply_text(translate_init_text)

    async def unknown(self, update, context):
        # if user write unknown command(/command), bot send this message
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Sorry, I didn't understand that command.")

    async def currency_exchange(self):
        text = ""
        message = self.update.message.text
        user = self.update.effective_user.username
        try:
            amount = int(message.split(":")[1].strip())
            if "in" in message:
                start_currency, end_currency = message.split(":")[0].strip().split(" in ")[0].split(" to ")
                year = message.split(":")[0].split(" in ")[1]
                try:
                    exchange_value = get_currency_history(start_currency.replace(" ", ""), end_currency.replace(" ", ""), int(year))
                    text = f"{start_currency} -->> {end_currency} in {year}" \
                           f"\n1 {start_currency} = {exchange_value:.2f} {end_currency} [Exchange currency]" \
                           f"\n{amount} {start_currency} = {float(exchange_value) * amount:.2f} {end_currency} [Your]"
                except KeyError:
                    text = "Cannot compare currencies in this year"
                self.print_text = f"[Currencies] {user} get info about currencies {start_currency} : {end_currency} in {year}"
            else:
                start_currency, end_currency = message.split(":")[0].strip().split(" to ")
                exchange_value = convert_currency(start_currency, end_currency, amount)
                text = f"{start_currency} -->> {end_currency}" \
                       f"\n1 {start_currency} = {float(exchange_value)/amount:.2f} {end_currency} [Exchange currency]" \
                       f"\n{amount} {start_currency} = {exchange_value:.2f} {end_currency} [Your]"
                self.print_text = f"[Currencies] {user} get info about currencies {start_currency} : {end_currency}"
        except (ValueError, IndexError) as err:
            print(err)
            text = "Something went wrong, try again!"

        self.currency = False
        return text

    async def currency_handle(self, update, context):
        await update.message.reply_text(currency_init_text)
        self.currency = True

    async def password_handle(self, update, context):
        await update.message.reply_text(password_init_text)
        self.password = True
        self.count_pass = 0

    async def password_action(self):
        message = self.update.message.text
        if message == "q":
            self.password = False
            await self.update.message.reply_text(start_init_text)
        else:
            user = self.update.effective_user.username
            dir_path = f"other_files/users_passwords/{user}"

            key_path = dir_path + f"/{user}.key"
            pass_path = dir_path + f"/{user}.pass"

            check_key = os.path.isfile(key_path)
            check_passwords = os.path.isfile(pass_path)

            if "=" in message or "get" in message or "delete" in message:
                if not check_key:
                    os.mkdir(dir_path)
                    pm.create_key(key_path)

                pm.load_key(key_path)

                if "=" in message:
                    site, password = message.split(" = ")
                    if not check_passwords:
                        pm.create_file(pass_path, initial_values={site: password})
                    else:
                        pm.add_password(site, password)
                    pass_text = "Password successfully added"
                    print(f"[Passwords] {user} add password ({site} = {password})")
                else:
                    try:
                        message_split = message.split(" ")
                        if "get" in message:
                            if len(message_split) > 1:
                                pass_text = pm.get_password(pass_path, message_split[1])
                            else:
                                pass_text = pm.get_beautiful_passwords(pass_path)

                            print(f"[Passwords] {user} get password(s)")
                        else:
                            if len(message_split) > 1:
                                pass_text = f"Password({message_split[1]}) successfully deleted."
                                pm.delete_password(message_split[1], pass_path)
                            else:
                                pass_text = "All passwords deleted"
                                pm.delete_all(pass_path)
                            print(f"[Passwords] {user} delete password(s)")

                    except FileNotFoundError as err:
                        pass_text = "Passwords file is empty" \
                                    "\nFirstly add one password with command:\n*site* = *password*"
                await self.update.message.reply_text(pass_text)
            else:
                self.count_pass += 1
                text = "Choose command above."
                if self.count_pass % 4 == 0:
                    text = password_init_text
                await self.update.message.reply_text(text)

    async def translate_handle(self) -> str:
        message = self.update.message.text
        text = ""
        try:
            if self.trans:
                self.languages = message.split(" to ")
                text = "Write text that will be translated"
                self.trans = False
                self.print_text = f"[Translate] {self.print_text}"
            elif len(self.languages) == 2:
                if len(message.split(" ")) == 1:
                    text = PonsTranslator(source=self.languages[0], target=self.languages[1]) \
                        .translate(message, return_all=True)
                    text = f"Основной перевод: {text[0]}\nСинонимы: {text[1:]}"
                else:
                    text = GoogleTranslator(source=self.languages[0], target=self.languages[1]) \
                        .translate(message)
                self.print_text = f"[Translated] {self.print_text}: {text}"
                self.languages = ()
        except LanguageNotSupportedException as ex:
            print(ex)
            self.print_text = f"[Error] Language is not supported"
            text = "Some language not supported, try again!"
        return text

    async def keyboard_handle(self) -> str:
        text = ""
        message = self.update.message.text
        user = self.update.effective_user.username

        if message in keyboards_buttons or self.check_random:
            if message == "Throw dice":
                await self.update.message.reply_dice(emoji="🎲")
                text = f"Dice is thrown, you can see result!"
                self.print_text = f"[Buttons] {user} throw dice"
            elif message == "Random number" or self.check_random:
                if self.check_random:
                    await self.update.message.reply_dice(emoji="🎲")
                    number1, number2 = message.split(" to ")
                    random_num = random.randint(int(number1), int(number2))
                    text = f"Your number: {random_num}"
                    time.sleep(4)
                    self.print_text = f"[Buttons] {user} get random number: {random_num}"
                else:
                    text = "Write frames in format:\n*number 1* to *number 2*"
                self.check_random = not self.check_random
            else:
                text = "Rate the photo"
                self.markup = InlineKeyboardMarkup([
                    [InlineKeyboardButton("👍", callback_data="like")],
                    [InlineKeyboardButton("👎", callback_data="dislike")]])

                if message == "Random image":
                    image = requests.get(random_image).content
                    self.print_text = f"[Buttons] {user} want a random image"
                else:
                    image = requests.get(random_person_image).content
                    self.print_text = f"[Buttons] {user} want a random person image"
                media_photo = InputMediaPhoto(image, caption="")
                await self.context.bot.sendMediaGroup(chat_id=self.update.effective_chat.id, media=[media_photo])
        return text

    async def time_notify(self, update, context):
        await update.message.reply_text(notify_init_text)
        self.notify = True

    async def start_daily_notify(self, message, user_text):
        week_day = message.split(" ")[0]
        hour, minute = message.split(" ")[1].split(":")
        await self.update.message.reply_text(f"In {week_day} at time {hour}:{minute} will play alert with task:\n"
                                             f"{user_text}")

        print(f"[Notifier] In {week_day} at time {hour}:{minute} we will bother {self.update.effective_user.username}😈")
        notifier = Notifier(f"COME ON DO THIS TASKS\n>>  {user_text}  <<\nI will bother you😈", self.update)
        self.context.job_queue.run_daily(notifier.alert_message,
                                         datetime.time(hour=int(hour), minute=int(minute),
                                                       tzinfo=pytz.timezone('Europe/Tallinn')),
                                         days=(get_week_day(week_day),))

    async def start_every_notify(self, message, user_text):
        split = message.split(" ")
        amount = int(split[0]) if len(split) > 1 else 1
        new_amount = amount

        time_type = "second"
        if "minute" in message:
            new_amount = amount * 60
            time_type = "minute"
        elif "hour" in message:
            new_amount = amount * 3600
            time_type = "hour"
        await self.update.message.reply_text(f"Every {amount} {time_type} will play alert with task:\n"
                                             f"{user_text}")

        print(f"[Notifier] Every {amount} {time_type} we will bother {self.update.effective_user.username}😈")
        notifier = Notifier(f"COME ON DO THIS TASKS\n>>  {user_text}  <<\nI will bother you😈", self.update)
        self.context.job_queue.run_repeating(notifier.alert_message, new_amount)

    async def notify_handle(self):
        message = self.update.message.text

        if message == "stop":
            await self.context.job_queue.stop()
            await self.update.message.reply_text(f"All alerts({len(self.context.job_queue.jobs())}) was stopped!!!")
        elif message == "quit":
            self.notify = False
        elif self.notify_message != "":
            if ":" in self.notify_message:
                await self.start_daily_notify(self.notify_message, message)
            elif "second" in self.notify_message or "minute" in self.notify_message or "hour" in self.notify_message:
                await self.start_every_notify(self.notify_message, message)
            else:
                await self.update.message.reply_text(notify_init_text)
            self.notify_message = ""
        else:
            if ":" in message or "second" in message or "minute" in message or "hour" in message:
                self.notify_message = message
                await self.update.message.reply_text("Write TODO or description for alert...")
            else:
                await self.update.message.reply_text(notify_init_text)

    async def handle(self, update, context):
        message = update.message.text
        self.update = update
        self.context = context

        self.markup = None
        text = ""
        self.print_text = f"{update.effective_user.username} write - " + message

        trans_handle = await self.translate_handle()
        key_handle = await self.keyboard_handle()

        if self.echo_run:
            self.print_text = f"[Echo] {self.print_text}"
            text = message
        elif trans_handle != "":
            text = trans_handle
        elif key_handle != "":
            text = key_handle
        elif self.currency:
            text = await self.currency_exchange()
        elif self.password:
            await self.password_action()
        elif self.notify:
            await self.notify_handle()
        else:
            text = start_init_text

        if text != "":
            print(self.print_text)
            await update.message.reply_text(text, reply_markup=self.markup)

    async def callback_handle(self, update, context):
        query = update.callback_query.data
        if "like" in query:
            await update.callback_query.answer()

            if "like" == query:
                self.likes += 1
            elif "dislike" == query:
                self.dislikes += 1

            await update.callback_query.edit_message_text(text="Rate the photo", reply_markup=None)
            print(f"[Rating] -> Total: likes={self.likes}, dislikes={self.dislikes}")
        else:
            await additional_que.list_button(update, context)


if __name__ == '__main__':
    telegram_bot = TelegramBot()

    app = (Application.builder()
           .token(telegram_token)
           .build())

    app.add_handlers([
        CommandHandler("start_buttons", telegram_bot.start_buttons),
        CommandHandler("echo", telegram_bot.echo),
        CommandHandler("que", additional_que.questionnaire),
        CommandHandler("anekdot", telegram_bot.get_anekdot),
        CommandHandler("translate", telegram_bot.translate),
        CommandHandler("currency_exchange", telegram_bot.currency_handle),
        CommandHandler("passwords", telegram_bot.password_handle),
        CommandHandler("notifier", telegram_bot.time_notify),
        MessageHandler(filters.TEXT & ~filters.COMMAND, telegram_bot.handle),
        MessageHandler(filters.COMMAND, telegram_bot.unknown),
        InlineQueryHandler(inline_caps),
        CallbackQueryHandler(telegram_bot.callback_handle),
        CallbackQueryHandler(additional_que.handle_invalid_button, pattern=InvalidCallbackData)
    ])

    app.run_polling()

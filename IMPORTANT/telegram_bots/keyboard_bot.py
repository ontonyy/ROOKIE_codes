import telebot
from telebot import types
import random

def telegram_bot(token):
    # Bot starting
    bot = telebot.TeleBot(token)
    
    # Start button
    @bot.message_handler(commands=['start'])
    def start_message(message):
        # Greeting sticker
        sticker = open('projects\IMPORTANT/telegram_bots/telegram_stickers_pics\hello_pic.webp', 'rb')
        bot.send_sticker(message.chat.id, sticker)

        # First down buttons
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Random number')
        item2 = types.KeyboardButton('How are you bot?')
        markup.add(item1, item2)

        # Message and buttons adding
        bot.send_message(message.chat.id, 'Welcome, {0.first_name}'.format(message.from_user),
                        reply_markup=markup)

    # Some text from user, and some responses from bot
    @bot.message_handler(content_types=['text'])
    def message_send(message):
        if message.chat.type == 'private':
            if message.text == 'Random number':
                bot.send_message(message.chat.id, str(random.randint(1, 100)))
            elif message.text == 'How are you bot?':
                # Question and buttons nearly
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton('All is good', callback_data='good')
                item2 = types.InlineKeyboardButton('Not so good', callback_data='bad')
                markup.add(item1, item2)

                bot.send_message(message.chat.id, 'I am fine, AND I AM BOT.\nNow how are you bot :) ?', reply_markup=markup)
            else:
                bot.send_message(message.chat.id, 'Hm I don\'t understood, I am a bot, like youOOOUUUUUUUUU!')

    # Second response from bot
    @bot.callback_query_handler(func=lambda call: True)
    def callback_inline(call):
        try:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'WOW really good!')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Ouu it is temporary')
            
            # Inline buttons removing, after answering
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                                text='How are you?', reply_markup=None)
            
            # Show some alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                    text='Thx for response!')

        except Exception as ex:
            print(ex)
    bot.polling(none_stop=True, interval=0)

if __name__ == '__main__':
    telegram_bot('1823572384:AAE5Fs-RqoOZXEsWkbdgbVUReD1ijiqxDFQ')

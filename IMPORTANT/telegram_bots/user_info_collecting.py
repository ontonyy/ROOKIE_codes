import telebot
from telebot import types

name = ''
surname = ''
age = 0

def telegram_bot(token):
    bot = telebot.TeleBot(token)
    print('Bot is starting work...')

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'Hello, {0.first_name}!\nTo start write "info"!!'.format(message.from_user))

    @bot.message_handler(content_types=['text'])
    def info_check(message):
        if message.text == 'info':
            bot.send_message(message.from_user.id, 'Write your name: ')
            bot.register_next_step_handler(message, get_name)
        else:
            bot.send_message('Check the rules or write "info"')

    def get_name(message):
        global name
        name = message.text
        bot.send_message(message.from_user.id, 'Write your surname: ')
        bot.register_next_step_handler(message, get_surname)

    def get_surname(message):
        global surname
        surname = message.text
        bot.send_message(message.from_user.id, 'What is your age?')
        bot.register_next_step_handler(message, get_age)

    def get_age(message):
        global age
        while age == 0:
            try:
                age = int(message.text)
            except Exception:
                bot.send_message(message.from_user.id, 'Age in integers please!')
        bot.send_message(message.from_user.id, f'Your name: {str(name)}\
                                                \nSurname: {str(surname)}\
                                                \nAge: {str(age)}'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    )
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('YEAASS!', callback_data='yes')
        item2 = types.InlineKeyboardButton('NOPE dude!', callback_data='no')
        markup.add(item1, item2)

        bot.send_message(message.chat.id, 'Is it right info?!', reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):
        try:
            if call.data == 'yes':
                bot.send_message(call.message.chat.id, 'I am really glad, see that!')
            elif call.data == 'no':
                bot.send_message(call.message.chat.id, 'On vaja teha seda uuesti!\n-----> "info"')
            
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='OMG, OMG, dudos is starting...')

        except Exception as ex:
            print(ex)

    bot.polling()

if __name__ == '__main__':
    telegram_bot('1876846708:AAFb3z652q--i8jiQdPYDy6rTioWzcWjvsA')

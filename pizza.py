import telebot

bot = telebot.TeleBot ('6752302597:AAGI9PzbF5-qmZeT_xukHApG4TAGweyG9O4')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,'Привет!')


bot.polling(none_stop=True)

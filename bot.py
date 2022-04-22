# start bot
import telebot

TOKEN = '5162584850:AAHgbosIOJZDrEZnS6x2EhngE3pUWubV_GA'

bot = telebot.TeleBot(TOKEN, parse_mode=None)  # You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(content_types=['text'])

def send_echo(message):
    print(message)
    bot.reply_to(message, 'Priv:' + message.from_user.username)


bot.polling()

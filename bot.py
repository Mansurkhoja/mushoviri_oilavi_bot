# start bot
import telebot

TOKEN = '5162584850:AAHgbosIOJZDrEZnS6x2EhngE3pUWubV_GA'

bot = telebot.TeleBot(TOKEN, parse_mode=None)  # You can set parse_mode by default. HTML or MARKDOWN

arrQA = [
    {'question': 'что то', 'answer': 'ы'},
    {'question': 'ллл', 'answer': 'й'},
    {'question': 'ллыл', 'answer': 'ыфы'}
]


@bot.message_handler(content_types=['text'])
def send_echo(message):
    print(message)
    d = next((x for x in arrQA if
              x['question'].capitalize().replace(" ", "") == message.text.capitalize().replace(" ", "")),
             None)
    if d is None:
        bot.reply_to(message, '((')
    else:
        bot.reply_to(message, d['answer'])


bot.polling()

# start bot
import telebot

from constants import TOKEN

bot = telebot.TeleBot(TOKEN, parse_mode=None)  # You can set parse_mode by default. HTML or MARKDOWN

arrQA = [
    {'question': 'Салом', 'answer': 'Салом'},
    {'question': 'Пеш аз оиладоршави чиро донистан лозим аст',
     'answer': '1) вазъияти саломатии якдигар \n2) такрибан характери якдигар \n3) шароити оилавии якдигар \n4) '
               'хукук ва ухдадории зану шавхар'},
    {'question': 'Оиди вазъияти саломатии якдигар',
     'answer': '1.1. Дорои ягон касалии рухи ва чисмони; 1.2. Гузаштани муоинаи духтур; 1.3. Нуксони намудор ва ё '
               'ноаён (гирифтани забон, олуси, касалии пуст...)'},
    {'question': 'Оиди донистани характери якдигар',
     'answer': '2.1. Чи гуна завча/шавхари худро дар оянда дидан мехохед? 2.2.Падар ва модари домод, '
               'чи гуна муносибатро аз келини худ интизор мешаванд? 2.3. Падар ва модари арус чи?'}
]


@bot.message_handler(content_types=['text'])
def send_echo(message):
    print(message)
    d = next((x for x in arrQA if
              x['question'].capitalize().replace(" ", "") ==
              message.text.capitalize().replace(" ", "").replace("?", "").replace(".", "").replace(":", "")),
             None)
    if d is None:
        bot.reply_to(message, '((')
    else:
        bot.reply_to(message, d['answer'])


bot.polling()

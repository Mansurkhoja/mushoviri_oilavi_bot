# This is a sample Python Telegram Bot.

# bot_token(TOKEN)

BOT_NAME = 'mushoviri_oilavi_bot'


def bot_name(name):
    print(f'bot name is: {name}')


# bot_name(BOT_NAME)

def bot_info():
    print('Bot Info:')
    bot_name(name=BOT_NAME)


bot_info()


def testF(**arg):
    # for i in arg:
    #     print(arg[i])
    print(arg, len(arg))
    if 'w' in arg:
        print(arg['w'])


testF(k='e', w=1)


class Car:

    # init method or constructor
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def show(self):
        print("Model is", self.model)
        print("color is", self.color)


# both objects have different self which
# contain their attributes
audi = Car("audi a4", "blue")

audi.show()

# start bot
import telebot

TOKEN = '5162584850:AAHgbosIOJZDrEZnS6x2EhngE3pUWubV_GA'

bot = telebot.TeleBot(TOKEN, parse_mode=None)  # You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "M")


bot.polling()

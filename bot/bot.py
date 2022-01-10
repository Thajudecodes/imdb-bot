from telebot import TeleBot
from bot.imdb_provider import IMDBProvider
import os

bot = TeleBot(token=os.getenv('5072010954:AAEMKqVfop1pwoGtvMwoLFLJqOQRxgX7vN8'))
imdb = IMDBProvider()


@bot.message_handler(commands=['get_movie_info'])
def get_movie_title(message):
    msg = bot.reply_to(message, 'What movie are you interested in?\nFormat -> title-year')
    bot.register_next_step_handler(message=msg, callback=send_movie_info)


def send_movie_info(message):
    results = imdb.get_movies_ids(movie_str=message.text)
    prepare_output(data=results)
    # bot.reply_to(message, result)


def prepare_output(data):
    # output = ''
    # import pprint
    # for item in data:
    #     pprint.pprint(item)
    print(data)

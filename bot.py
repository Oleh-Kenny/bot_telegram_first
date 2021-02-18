# import telebot
# import random 
# from telebot import types
# bot = telebot.TeleBot('1175624099:AAGwuiCjWSHrZYVZkD-kzv4oPS15Oo9ZEM8')
# name = ''
# surname = ''
# age = 0
# @bot.message_handler(content_types=['text', 'document', 'audio'])

# def start(message):
#     if message.text == '/reg':
#         bot.send_message(message.from_user.id, " Привіт, Як тебе звати?")
#         bot.register_next_step_handler(message, get_name)
#     else:
#         bot.send_message(message.from_user.id, "Напиши /reg")

# def get_name(message):
#     global name
#     name = message.text
#     bot.send_message(message.from_user.id, "Яка в тебе фамілія?")
#     bot.register_next_step_handler(message, get_surname)

# def get_surname(message):
#     global surname
#     surname = message.text
#     bot.send_message( message.from_user.id, 'Скільки тобі років?')
#     bot.register_next_step_handler(message, get_age)

# def get_age(message):
#     global age
#     while age == 0:
#         try:
#             age = int(message.text)
#         except Exception:
#             bot.send_message(message.from_user.id, "Цифри будь ласка")
#     keyboard = types.InlineKeyboardMarkup()#наша клавиатура
#     key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes') #кнопка «Да»
#     keyboard.add(key_yes)#добавляем кнопку в клавиатуру
#     key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
#     keyboard.add(key_no)
#     key_redag= types.InlineKeyboardButton(text='redag', callback_data='redag')
#     keyboard.add(key_redag)

#     question = "Тебе " +str(age)+ "років, тебе звати " +name+ " "+surname+ "?"
#     bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

# def random_game(message):
#     if message.text == 'Random':
#         bot.send_message(message.chat.id, str(random.randint(0,100)))

# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
#     if call.data == "yes":
#         bot.send_message(call.message.chat.id, "Запамятаю :)")
#     elif call.data == "no":
#         bot.send_message(call.message.chat.id, "Тебе " +str(age)+ "років, тебе звати " +name+ " "+surname+ "?")
#     elif call.data == "redag":
#         bot.send_message(call.message.chat.id, "Тоді редагуємо - натисни /reg")
    

# bot.polling(none_stop=True, interval=0)


# from telegram.ext import Updater, InlineQueryHandler, CommandHandler
# from telegram.ext.dispatcher import run_async
# import requests
# import re

# def get_url():
#     contents = requests.get('https://random.dog/woof.json').json()
#     url = contents['url']
#     return url

# def get_image_url():
#     allowed_extension = ['jpg','jpeg','png']
#     file_extension = ''
#     while file_extension not in allowed_extension:
#         url = get_url()
#         file_extension = re.search("([^.]*)$",url).group(1).lower()
#     return url

# @run_async
# def bop(update, context):
#     url = get_image_url()
#     chat_id = update.message.chat_id
#     context.bot.send_photo(chat_id=chat_id, photo=url)

# def main():
#     updater = Updater('1175624099:AAGwuiCjWSHrZYVZkD-kzv4oPS15Oo9ZEM8', use_context=True)
#     dp = updater.dispatcher
#     dp.add_handler(CommandHandler('bop',bop))
#     updater.start_polling()
#     updater.idle()

# if __name__ == '__main__':
#     main()

# ----------------------------------------------------------------------------------

import telebot
import requests
from modul import config
from bs4 import BeautifulSoup as BS
from telebot import types

bot = telebot.TeleBot(config.TOKEN)
response = requests.get(config.url).json()

@bot.message_handler(commands=['start', 'help'])
def main(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        itembtn1 = types.KeyboardButton('Погода')
        itembtn2 = types.KeyboardButton('Курсы валют')

        markup.add(itembtn1, itembtn2)
        msg = bot.send_message(message.chat.id, "Привет, выберите действие", reply_markup=markup)
        bot.register_next_step_handler(msg, process_switch_step)

def process_switch_step(message):
        if (message.text == 'Погода'):
            weather(message)
            main(message)
        elif (message.text == 'Курсы валют'):
            coins(message)

def weather(message):
        '''Эта функция погоды'''

        markup = types.ReplyKeyboardRemove(selective=False)

        r = requests.get('https://ua.sinoptik.ua/погода-рівне')
        html = BS(r.content, 'html.parser')

        for el in html.select('#content'):
            t_day1 = el.select('.tabs #bd1')[0].text
            t_day2 = el.select('.tabs #bd2')[0].text
            t_day3 = el.select('.tabs #bd3')[0].text
            t_day4 = el.select('.tabs #bd4')[0].text
            t_day5 = el.select('.tabs #bd5')[0].text
            t_day6 = el.select('.tabs #bd6')[0].text
            t_day7 = el.select('.tabs #bd7')[0].text
            # t_min = el.select('.temperature .min')[0].text
            # t_max = el.select('.temperature .max')[0].text
            # text = el.select(' .wDescription ')[0].text
            # text2 = el.select(' .wDescription ')[0].text
        
        bot.send_message(message.chat.id, "Привет, погода на тиждень:\n" +t_day1+ '------------''\n'+t_day2+'------------''\n'+t_day3+ '------------''\n'+t_day4+'------------''\n'+t_day5+'------------''\n'+t_day6+ '------------''\n'+t_day7+'------------''\n', reply_markup=markup)


def coins(message):
        '''Эта функция курсы валют'''
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        itembtn1 = types.KeyboardButton('USD')
        itembtn2 = types.KeyboardButton('EUR')
        itembtn3 = types.KeyboardButton('RUR')
        itembtn4 = types.KeyboardButton('BTC')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4)

        msg = bot.send_message(message.chat.id, 
                        "Узнать наличный курс ПриватБанка (в отделениях)", reply_markup=markup)
        bot.register_next_step_handler(msg, process_coin_step)

def process_coin_step(message):
        try:
            markup = types.ReplyKeyboardRemove(selective=False)

            for coin in response:
                if (message.text == coin['ccy']):
                    bot.send_message(message.chat.id, printCoin(coin['buy'], coin['sale']), 
                                    reply_markup=markup, parse_mode="Markdown")

            main(message)

        except Exception as e:
            bot.reply_to(message, 'ooops!')

def printCoin(buy, sale):
        '''Вывод курса пользователю'''

        return "💰 *Курс покупки:* " + str(buy) + "\n💰 *Курс продажи:* " + str(sale)

# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling(none_stop=True)
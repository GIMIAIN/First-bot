from api_controller import response
import telebot
import requests

bot = telebot.TeleBot("5246671614:AAE2cTjj4g_V2KqNZQP28F-srrnu_t_umUQ")

name = ''
surname = ''
age = 0
hobbie = ''

@bot.message_handler(content_types=['text'])
def start_dialog(message):
    if message.text == '/start' or message.text == '/help':
        bot.send_message(message.from_user.id, response)

bot.infinity_polling()
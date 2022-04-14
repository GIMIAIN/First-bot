import telebot
import api_controller

bot = telebot.TeleBot("5246671614:AAE2cTjj4g_V2KqNZQP28F-srrnu_t_umUQ")

name = ''
surname = ''
age = 0
hobbie = ''

@bot.message_handler(content_types=['text'])
def start_dialog(message):
    if message.text == '/start' or message.text == '/help':
        bot.reply_to(message, 'Здравствуй, человек!')
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)

def get_name(message): #получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
    age = message.text
    bot.send_message(message.from_user.id, 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?')
    bot.register_next_step_handler(message, answer_1)

def answer_1(message):
    if message.text == 'да' or message.text == 'Да':
        bot.send_message(message.from_user.id, 'Классно, я молодец)')
    elif message.text == 'нет' or message.text == 'Нет':
        bot.send_message(message.from_user.id, 'Ошибочка вышла')
    bot.send_message(message.from_user.id, 'А чем такой хороший человек занимается?')
    bot.register_next_step_handler(message, get_hobbie)

def get_hobbie(message): #получаем хобби
    global hobbie
    hobbie = message.text
    bot.send_message(message.from_user.id, 'Ой, а мне ведь тоже нравится заниматься '+hobbie+'!')
    bot.register_next_step_handler(message, get_hobbie)

def 



bot.infinity_polling()
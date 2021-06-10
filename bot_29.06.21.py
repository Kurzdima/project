import telebot
import telebot.types

bot = telebot.TeleBot('1808104531:AAFbhg77kO_RX5dMy1ohF9TzNOzbVp12-20')

@bot.message_handler(content_types=['text'])
def handle_start(message):
    if message.text == "Привет":

bot.send_message(message.from_user.id, "Привет, чем я могу вам помочь?")

elif message.text == "/help":

bot.send_message(message.from_user.id, "Напишите привет")

else:

bot.send_message(message.from_user.id, "Я вас не понимаю. Напиши /help.")
name = '';

profession = '';

phone = 0;

@bot.message_handler(content_types=['text'])

def start(message):

if message.text == '/reg':

bot.send_message(message.from_user.id, "Напишите вашу фамилию/имя?");

bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name

else:

bot.send_message(message.from_user.id, 'Напишите ваше имя и фамилию/reg');



def get_name(message): # узнаем должность

global name;

name = message.text;

bot.send_message(message.from_user.id, 'Какая у вас должность?');

bot.register_next_step_handler(message, get_profession);



def get_profession(message):

global profession;

profession = message.text;

bot.send_message('Напишите номер, по которому с вами можно связаться?');

bot.register_next_step_handler(message, get_phone);



def get_phone(message):

global phone;

while phone == 0: #проверяем что телефон изменился

try:

phone = int(message.text) #проверяем, что телефон введён корректно

except Exception:

bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');

bot.send_message(message.from_user.id, 'Номер для связи '+str(phone)+' , вас зовут '+name+', '+profession+'?')

bot.polling(none_stop=True, interval=0)
print(123)

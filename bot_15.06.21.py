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

bot.polling(none_stop=True, interval=0)
print(123)

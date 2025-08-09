import telebot
import chatgpt

bot = telebot.TeleBot("2014017704:AAEBXiQZSmgnwv-NJIyraANUCUy__QHRNRM")


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Hi, how may I assist you?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    response = chatgpt.ask_ai(message.text)
    bot.send_message(message.chat.id, response)


bot.infinity_polling()

import telebot
import chatgpt

bot = telebot.TeleBot("8472626435:AAH3K0iL3uRxRo8M8xYJXL5I2zkK82str8k")


def send_welcome(message):
    bot.reply_to(message, "Hi, how may I assist you?")


def help(message):
    bot.reply_to(message, "for help contact 0918")


def echo_all(message):
    # bot.send_message(message.chat.id, "123")
    response = chatgpt.ask_ai(message.text)
    bot.send_message(message.chat.id, response)


bot.register_message_handler(send_welcome, commands=['start'])
bot.register_message_handler(help, commands=['help'])
bot.register_message_handler(echo_all, func=lambda message: True)

bot.infinity_polling()

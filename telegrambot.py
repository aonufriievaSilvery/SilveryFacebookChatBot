import telebot
from telebot import types

bot = telebot.TeleBot("5611189386:AAHw2FeF_tZ0yXZIhTh3UJTBAST_h3eiQWU")


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("About")
    btn2 = types.KeyboardButton("AnotherText")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Hello", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def func(message):
    if message.text == "About":
        bot.send_message(message.chat.id, text="Above my head")
    elif message.text == "AnotherText":
        bot.send_message(message.chat.id, text="Above my another head")
    else:
        bot.send_message(message.chat.id, text="Choose button to speak with my another head!")


bot.infinity_polling()
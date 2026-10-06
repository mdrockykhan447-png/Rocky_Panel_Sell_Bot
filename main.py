import os
import telebot
from telebot import types

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📦 Panel Price", callback_data="price"))
    markup.add(types.InlineKeyboardButton("💬 Admin", url="https://t.me/mdrockykhan69"))
    bot.send_message(m.chat.id, "Welcome to Rockys Panel Sell Bot jan! 😊", reply_markup=markup)

@bot.callback_query_handler(func=lambda c: True)
def call(c):
    if c.data == "price":
        bot.send_message(c.message.chat.id, "🔥 Panel List:\nBasic - 300 Tk\nPremium - 600 Tk\n\nKinte /buy likho!")

@bot.message_handler(commands=['buy'])
def buy(m):
    bot.send_message(m.chat.id, "Buy korte Admin @mdrockykhan69 ke message dao jan!")

bot.infinity_polling()

import os
from flask import Flask
from threading import Thread
import telebot

TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

app = Flask('')

@app.route('/')
def home():
    return "Kicker FX Bot is Alive!"

def run():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك في بوت Kicker FX للخدمات الرياضية! 🚀")

if __name__ == "__main__":
    keep_alive()
    print("Bot is running...")
    bot.infinity_polling()
    

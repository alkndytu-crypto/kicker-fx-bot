import os
import telebot

# استدعاء توكن البوت من بيئة التشغيل أو وضعه هنا مباشرة
TOKEN = os.getenv('BOT_TOKEN', 'YOUR_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك يا تركي في بوت Kicker FX لتعديل وعمل صانعي المحتوى الرياضي! البوت يعمل بنجاح 24/7.")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "أرسل أي فيديو أو رابط لتطبيق التأثيرات والأدوات المتاحة.")

if __name__ == '__main__':
    print("Bot is running...")
    bot.infinity_polling()
  

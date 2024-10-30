import telebot

TOKEN = "YOUR_TELEGRAM_TOKEN"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я помогу вам с отслеживанием привычек!")

bot.polling()

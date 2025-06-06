from loader import bot

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет')

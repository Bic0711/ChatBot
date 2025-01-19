from telebot.types import Message
from keyboards.inline.choose_search_option import kb_search_options
from loader import bot

@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    welcome_text = (
        f"Привет {message.from_user.full_name}, я Rut_Moovie Bot.\n"
        "Я помогу тебе найти фильм.\n\n"
        "Вот доступные кнопки:"
    )
    bot.reply_to(message, welcome_text, reply_markup=kb_search_options())
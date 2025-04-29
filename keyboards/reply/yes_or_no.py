from telebot.types import ReplyKeyboardMarkup,KeyboardButton

def yes_no_kb()->ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    kb.add(KeyboardButton("Да"), KeyboardButton("Нет"))
    return kb
from api.commands.get_response import get_response
from loader import bot
from states.user_state import UserInfoState
from telebot.types import CallbackQuery, Message

from utils.misc.param_setup import param_setup
global SEARCH_STATE, SEARCH_INFO

@bot.callback_query_handler(func=lambda call: True)
def bot_answer(call: CallbackQuery):
    global SEARCH_STATE, SEARCH_INFO
    if call.data == "search_random":
        bot.set_state(call.from_user.id, UserInfoState.random, call.message.chat.id)
        bot.send_message(call.message.chat.id, "Показываю случайный фильм")
    elif call.data == "search_genre":
        bot.set_state(call.from_user.id, UserInfoState.genre, call.message.chat.id)
        bot.send_message(call.message.chat.id, "Введите жанр фильма")
    elif call.data == "search_year":
        bot.set_state(call.from_user.id, UserInfoState.year, call.message.chat.id)
        bot.send_message(call.message.chat.id, "Введите год фильма")
    elif call.data == "search_country":
        bot.set_state(call.from_user.id, UserInfoState.country, call.message.chat.id)
        bot.send_message(call.message.chat.id, "Введите страну фильма")
    elif call.data == "search_actor":
        bot.set_state(call.from_user.id, UserInfoState.actor, call.message.chat.id)
        bot.send_message(call.message.chat.id, "Введите имя актера")
    elif call.data == "repeat_last_search":
        bot.send_message(call.message.chat.id, "Повторяю последний поиск")
        get_response(SEARCH_INFO,SEARCH_STATE.split(":")[1],param_setup(SEARCH_STATE.split(":")[1],search_info=SEARCH_INFO))



@bot.message_handler(state=[UserInfoState.genre, UserInfoState.year, UserInfoState.country, UserInfoState.actor])
def bot_answer(message: Message):
    global SEARCH_STATE, SEARCH_INFO
    SEARCH_INFO = message
    SEARCH_STATE = bot.get_state(message.from_user.id, message.chat.id)
    search_type = SEARCH_STATE.split(":")[1]
    bot.delete_state(message.from_user.id, message.chat.id)
    params = param_setup(search_type, search_info=SEARCH_INFO.text)
    get_response(message,search_type,params)
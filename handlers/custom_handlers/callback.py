from states.user_state import UserInfoState
from loader import bot
from telebot.types import CallbackQuery, Message
from api.commands.get_response import get_response


@bot.callback_query_handler(func=lambda call: "search" in call.data)
def call_back_search(call: CallbackQuery)-> None:
    user_id = call.from_user.id
    if call.data == "movie_search_random":
        bot.set_state(user_id, UserInfoState.random)
        bot.send_message(user_id,"Показываю рандомный фильм")
        get_response(search_type=call.data, message=call.message)



    elif call.data == "search_genre":
        bot.send_message(call.message.chat.id,"Введите жанр фильма:")
        bot.get_state(user_id)
        bot.set_state(user_id, UserInfoState.genre)
        bot.get_state(user_id)



    elif call.data == "search_year":
        bot.set_state(user_id, UserInfoState.year)
        bot.send_message(user_id,"Введите год фильма:")

    elif call.data == "search_country":
        bot.set_state(user_id, UserInfoState.country)
        bot.send_message(user_id,"Введите страну фильма:")

    elif call.data == "search_actor":
        bot.set_state(user_id, UserInfoState.actor)
        bot.send_message(user_id,"Введите имя актера:")

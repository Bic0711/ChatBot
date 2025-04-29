import requests
import os
from telebot.types import Message
from keyboards.reply.yes_or_no import yes_no_kb
from loader import bot

from states.user_state import UserInfoState
from utils.misc.param_setup import param_setup
from utils.misc.send_info_from_responce import send_info

# from utils.misc.show_movie import send_info

API_KEY = os.getenv("KINOPOISK_API_KEY")
HEADERS = {
    "accept": "application/json",
    "X-API-KEY": API_KEY
}
BASE_URL = "https://api.kinopoisk.dev/v1.4/"
user_data = {}
chosen_actor = 111


def get_response(message, search_type, params):
    response = None
    if search_type in ("genre", "year", "country", "random","movie"):
        response = requests.get(f"{BASE_URL}movie/random", headers=HEADERS, params=params)
    elif search_type == "actor":
        response = requests.get(f"{BASE_URL}person/search", headers=HEADERS, params=params)
    object_info = get_info_from_response(message, response.json(), search_type)
    return object_info


def get_info_from_response(message, response, search_type):
    object_info = {}
    if search_type in ("random", "genre", "year", "country","movie"):
        object_info["id"] = response["id"]
        object_info["name"] = response["name"]
        object_info["poster_url"] = response["poster"]["url"]
        object_info["description"] = [response["description"][i:i + 900] for i in
                                      range(0, len(response["description"]), 900)][0]
        object_info["year"] = response["year"]
        object_info["countries"] = ", ".join([country["name"] for country in response["countries"]])
        object_info["genres"] = ", ".join([genre["name"] for genre in response["genres"]])
        object_info["rating"] = response["rating"]["kp"]
        if object_info["poster_url"].startswith("https:https:"):
            object_info["poster_url"] = object_info["poster_url"][6:]
    elif search_type == "actor":
        actors_list = list(filter(lambda actor: actor['photo'], response["docs"]))
        result_dict = {
            actor['id']: (actor['name'], actor['photo'])
            for actor in actors_list
            if actor['photo']
        }
        send_actors_photo(message.chat.id, iter(result_dict.items()))

    return object_info


@bot.message_handler(state=UserInfoState.chose_actor)
def handle_response(message: Message):
    chat_id = message.chat.id
    actor_id = user_data.get(chat_id, {}).get('actor_id')  # Извлекаем actor_id

    if message.text == 'Да':
        params = param_setup(search_type="by_actor", search_info=actor_id)
        movie_info = get_response(message=message, search_type="movie", params=params)
        send_info(message, movie_info)
    elif message.text == 'Нет':
        # Получаем сохраненный итератор из user_data
        actor_iter = user_data.get(chat_id, {}).get('actor_iter')
        if actor_iter is None:
            # Если итератора нет, создаем новый
            actors_dict = {
                123: ("Имя актера 1", "https://example.com/photo1.jpg"),
                456: ("Имя актера 2", "https://example.com/photo2.jpg")
            }
            actor_iter = iter(actors_dict.items())
            user_data[chat_id] = {'actor_iter': actor_iter}  # Сохраняем итератор

        send_actors_photo(chat_id, actor_iter)
    else:
        bot.send_message(chat_id, 'Пожалуйста, ответьте "Да" или "Нет".')


def send_actors_photo(chat_id, actor_iter):
    try:
        actor_id, (name, photo_url) = next(actor_iter)
        if photo_url.startswith("https:https:"):
            photo_url = photo_url[6:]
        user_data[chat_id] = {'actor_id': actor_id, 'actor_iter': actor_iter}
        markup = yes_no_kb()
        bot.send_photo(chat_id, photo_url, caption=name, reply_markup=markup)
        bot.set_state(chat_id, UserInfoState.chose_actor, chat_id)
    except StopIteration:
        bot.send_message(chat_id, 'Актеры заканчиваются!')
        # Удаляем итератор из user_data, так как актеры закончились
        if chat_id in user_data:
            del user_data[chat_id]['actor_iter']

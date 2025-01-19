from keyboards.reply.yes_or_no import yes_no_kb
from loader import bot
from keyboards.inline.search_step import search_options
from telebot.types import Message


def send_info(search_type, chat_id, object_info):
    object_type = search_type.split("_")[0]
    if object_type == "movie":
        if len(object_info["movie_description"]) > 1000:
            object_info["movie_description"] = object_info["movie_description"][:900] + "..."

        poster = object_info.get(
            "movie_poster") or "https://vverh.digital/images/system/2023/12/5/d5f00276206f411a848d9cb8cdc65376.png"

        text = (
            f"{object_info.get('movie_name', 'Название неизвестно')} ({object_info.get('movie_year', 'Год неизвестен')})\n\n"
            f"Жанр: {object_info.get('movie_genre', 'Жанр неизвестен')}\n"
            f"Страна: {object_info.get('movie_country', 'Страна неизвестна')}\n"
            f"Рейтинг Кинопоиска: {object_info.get('movie_rating', 'Рейтинг неизвестен')}\n\n"
            f"{object_info.get('movie_description', 'Описание отсутствует')}"
        )
        kb = search_options(search_type)
        bot.send_photo(chat_id, photo=poster, caption=text, reply_markup=kb)


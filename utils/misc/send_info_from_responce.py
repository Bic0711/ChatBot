from keyboards.inline.choose_search_option import kb_search_options
from loader import bot


def send_info(message, object_info):
    if object_info.get("description") and len(object_info["description"]) > 1000:
        object_info["description"] = object_info["description"][0][:900] + "..."

    poster = object_info.get(
        "poster_url") or "https://vverh.digital/images/system/2023/12/5/d5f00276206f411a848d9cb8cdc65376.png"

    text = (
        f"*{object_info.get('name', 'Название неизвестно')}* ({object_info.get('year', 'Год неизвестен')})    ★{object_info.get('rating', 'Рейтинг неизвестен') if object_info.get('rating') != 0 else 'Рейтинг неизвестен'}★\n\n"
        f"Жанр: {object_info.get('genres', 'Жанр неизвестен')}\n"
        f"Страна: {object_info.get('countries', 'Страна неизвестна')}\n\n"
        f"{object_info.get('description', 'Описание отсутствует')}"
    )

    bot.send_photo(message.chat.id, photo=poster, caption=text,parse_mode="Markdown", reply_markup=kb_search_options(show_movie_list_btn=True))

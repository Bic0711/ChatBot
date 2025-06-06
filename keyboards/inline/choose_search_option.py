from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def kb_search_options(show_movie_list_btn=False):
    kb = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text="Показать рандомный фильм.", callback_data="search_random")
    btn2 = InlineKeyboardButton(text="Показать фильм по жанру", callback_data="search_genre")
    btn3 = InlineKeyboardButton(text="Показать фильм по году", callback_data="search_year")
    btn5 = InlineKeyboardButton(text="Показать фильм по стране", callback_data="search_country")
    btn6 = InlineKeyboardButton(text="Показать фильм по актеру", callback_data="search_actor")
    show_movies_btn = InlineKeyboardButton(text="Показать список фильмов", callback_data="show_movie_list")

    repeat_last_search = InlineKeyboardButton(text="Повторить последний поиск", callback_data="repeat_last_search")
    kb.add(btn1, btn2, btn3, btn5, btn6)
    if show_movie_list_btn:
        kb.add(show_movies_btn, repeat_last_search)

    return kb

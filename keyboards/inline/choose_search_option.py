from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from states.user_state import UserInfoState

def kb_search_options(show_movie_list_btn=False, id_search=False):
    kb = InlineKeyboardMarkup(row_width=1)

    buttons = [
        InlineKeyboardButton(text="Показать рандомный фильм.", callback_data="movie_search_random",),
        InlineKeyboardButton(text="Показать фильм по жанру", callback_data="search_genre"),
        InlineKeyboardButton(text="Показать фильм по году", callback_data="search_year"),
        InlineKeyboardButton(text="Показать фильм по стране", callback_data="search_country"),
        InlineKeyboardButton(text="Показать фильм по актеру", callback_data="search_actor"),
    ]
    if show_movie_list_btn:
        buttons.append(InlineKeyboardButton(text="Показать список фильмов.", callback_data="show_movie_list"))

    if id_search:
        buttons.append(InlineKeyboardButton(text="id поиска", callback_data="id_search"))

    kb.add(*buttons)

    return kb
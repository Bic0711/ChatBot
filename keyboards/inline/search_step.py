from telebot import types


def search_options(repeat_search) -> types.InlineKeyboardMarkup:
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(
        text="  Сохранить фильм", callback_data="save_movie"
    )
    btn2 = types.InlineKeyboardButton(
        text="  Повторить поиск", callback_data=repeat_search
    )
    btn3 = types.InlineKeyboardButton(
        text="  Вернуться к выбору параметров поиска", callback_data="return_to_search_list"
    )

    kb.add(btn1, btn2, btn3)

    return kb
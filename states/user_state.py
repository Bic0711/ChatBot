from telebot.handler_backends import State, StatesGroup


class UserInfoState(StatesGroup):
    random = State()
    genre = State()
    year = State()
    country = State()
    actor = State()

    show_list = State()
    repeat_search = State()

    show_again = State()
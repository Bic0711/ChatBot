from telebot.handler_backends import State, StatesGroup

class UserInfoState(StatesGroup):
    random = State()
    genre = State()
    year = State()
    country = State()
    actor = State()
    start = State()
    chose_actor = State()
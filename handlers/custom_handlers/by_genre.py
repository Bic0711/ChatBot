from loader import bot
from states.user_state import UserInfoState
from telebot.types import Message


@bot.message_handler(state = UserInfoState.genre, content_types=['text'])
def get_movie_by_genre(message: Message) -> None:
    print(111)
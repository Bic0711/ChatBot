from loader import bot
import handlers.default_handlers.start  # noqa: F401

if __name__ == '__main__':
    bot.infinity_polling()

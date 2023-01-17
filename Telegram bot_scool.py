from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import CallbackContext


TOKEN = '5818310273:AAFy-hne3PSflIGU0gwrOfeZDZJAyrluKTI'


def main():
     #обьект, котрый ловит обновления
    updater = Updater(token=TOKEN)
     #Диспечер будет распределять события по обработчикам
    dispetcher = updater.dispatcher

     #Добавляем обработчик события из Telegram
    dispetcher.add_handler(
         CommandHandler('start', do_start)
    )
    dispetcher.add_handler(
         MessageHandler(Filters.text, do_echo)
     )

    # Бескончно просматривай обновления, пока работает код
    updater.start_polling()
    print(updater.bot.getMe)
    print('Бот запущен')
    updater.idle()


def do_start(update: Update, context: CallbackContext):
    text = 'Приветики, начнём?'
    update.message.reply_text(text)


def do_echo(update: Update, context: CallbackContext):
    text = update.message.text
    user_id = update.message.from_user.id
    name = update.message.from_user.name
    username = update.message.from_user.username
    text = f"Привет, {name}!\nТвой {username=}.\nТвой {user_id}.\n" + text
    context.bot.send_message(user_id, text)


if __name__ == '__main__':
    main()

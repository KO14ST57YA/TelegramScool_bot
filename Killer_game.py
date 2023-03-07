from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, ParseMode
from telegram.ext import Updater, updater
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import CallbackContext
from Key import TOKEN, ADMIN_AD



def main():
     #обьект, котрый ловит обновления
    updater = Updater(token=TOKEN)
     #Диспечер будет распределять события по обработчикам
    dispetcher = updater.dispatcher

     #Добавляем обработчик события из Telegram
    dispetcher.add_handler(CommandHandler('start', do_start))
    dispetcher.add_handler(CommandHandler('ask_for_name', ask_for_name))
    dispetcher.add_handler(MessageHandler(Filters.text, do_help))

    # Бескончно просматривай обновления, пока работает код
    updater.start_polling()
    print(updater.bot.getMe)
    print('Бот запущен')
    updater.idle()


def do_help(update: Update, context: CallbackContext):
    text = [
        'тестируем следующие функции: ',
        '/ask_for_class',
        '/ask_for_name',
        '/ask_for_photo',
        '/register_player',
    ]
    text = '\n'.join(text)
    update.message.reply_text(text)


def do_start(update: Update, context: CallbackContext):
    pass

def ask_for_class(update: Update, context: CallbackContext):
    pass

def ask_for_name(update: Update, context: CallbackContext):
    text = 'Напиши своё имя и фамилию'
    update.message.reply_text(text)


def ask_for_photo(update: Update, context: CallbackContext):
    pass

def register_player(update: Update, context: CallbackContext):
    pass

if __name__ == '__main__':
    main()



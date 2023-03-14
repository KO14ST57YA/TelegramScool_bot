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
    dispatcher = updater.dispatcher

     #Добавляем обработчик события из Telegram
    dispatcher.add_handler(CommandHandler('start', do_start))
    dispatcher.add_handler(CommandHandler('ask_for_class', ask_for_class))
    dispatcher.add_handler(CommandHandler('ask_for_name', ask_for_name))
    dispatcher.add_handler(CommandHandler('get_class', get_class))
    dispatcher.add_handler(MessageHandler(Filters.text, do_help))

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
    text = [
        'Введи номер своего класса.',
        'Для этого набери команду get_class и через пробел номер и букву класса.',
        'Например: /get_class 9н']
    text = '\n'.join(text)
    update.message.reply_text(text)


def get_class(update: Update, context: CallbackContext):
        grade = context.args
        # можно вывести содержимое переменной grade, чтобы понять, что туда попало
        print(grade)
        text = f'Я запомнил твой класс: {grade}'
        update.message.reply_text(text)
        return ask_for_name(update, context)




def ask_for_name(update: Update, context: CallbackContext):
    text = [
        'Введи имя и фамилию.',
        'Для этого набери команду get_name и имя и фамилию.',
        'Например: /get_name Константин Невский']
    text = '\n'.join(text)
    update.message.reply_text(text)



def get_name(update: Update, context: CallbackContext):
    name = context.args
    # можно вывести содержимое переменной name, чтобы понять, что туда попало
    print(name)
    text = f'Я запомнил твой класс: {name}'
    update.message.reply_text(text)
    return ask_for_photo(update, context)



def ask_for_photo(update: Update, context: CallbackContext):
    pass


def get_photo(update: Update, context: CallbackContext):
    pass


def register_player(update: Update, context: CallbackContext):
    all_spisok = []
    return all_spisok

if __name__ == '__main__':
    main()



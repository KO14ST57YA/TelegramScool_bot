from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, ParseMode
from telegram.ext import Updater
from telegram.ext import CommandHandler, ConversationHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import CallbackContext

from Key import TOKEN, ADMIN_AD
from connect_to_database import write_to_db

GRADES = (
    '8н', '8о', '8п', '8Н', '8О', '8П',
    '9н', '9о', '9п', '9Н', '9О', '9П',
    '10н', '10Н', '10но', '10НО',
    '11н', '11Н', '11о', '11О'
)
WAIT_FOR_CLASS, WAIT_FOR_NAME, WAIT_FOR_PHOTO = range(3)


def main():
     # обьект, котрый ловит обновления
    updater = Updater(token=TOKEN)
     # Диспечер будет распределять события по обработчикам
    dispatcher = updater.dispatcher

     # Добавляем обработчик события из Telegram
    dispatcher.add_handler(CommandHandler('start', do_start))
    dispatcher.add_handler(
        ConversationHandler(
            entry_points= [CommandHandler('register_player', ask_for_class)], # точки старта
            states = {
                WAIT_FOR_CLASS: [MessageHandler(Filters.text, get_class)],
                WAIT_FOR_NAME: [MessageHandler(Filters.text, get_name)],
                WAIT_FOR_PHOTO: [MessageHandler(Filters.text, get_photo)]}, # состояния
            fallbacks=[] # отлов ошибок
             )
    )

    dispatcher.add_handler(MessageHandler(Filters.text, do_help))

    # Бескончно просматривай обновления, пока работает код
    updater.start_polling()
    print(updater.bot.getMe)
    print('Бот запущен')
    updater.idle()


def do_help(update: Update, context: CallbackContext):

    text = [
        'Привет. Этот бот пока <i>много</i> чего не <s>умеет</s>!',
        'Но он запросто сможет тебя <u>зарегистрировать</u> :)',
        'Также лови ссылку на сайт нашей школы: <a href="1060.ru">Сайт школы</a>',
        f'Если будут вопросы, пиши сюда: @nevs_kostik'

    ]
    text = '\n'.join(text)
    update.message.reply_text(text, parse_mode=ParseMode.HTML, disable_web_page_preview=True)


def do_start(update: Update, context: CallbackContext):
    pass

def do_keyboard(update: Update, context: CallbackContext,): #Функция, которая создает клавиатуру
    buttons = [
        ['8н'], ['8о'], ['8п'], ['8Н'], ['8О'], ['8П'],
        ['9н'], ['9о'], ['9п'], ['9Н'], ['9О'], ['9П'],
        ['10н'], ['10Н'], ['10но'], ['10НО'],
        ['11н'], ['11Н'], ['11о'], ['11О']
        ]
    keyboard = ReplyKeyboardMarkup(buttons) # клавиатура класса ReplyKeyboardMarkup
    text = ':)'
    update.message.reply_text(text, reply_markup=keyboard)
    return keyboard

def ask_for_class(update: Update, context: CallbackContext):
    text = [
        'Ахалай махалай класс выбирай',
    ]

    text = '\n'.join(text)
    update.message.reply_text(text)
    do_keyboard(update, context)
    return WAIT_FOR_CLASS


def get_class(update: Update, context: CallbackContext):
    grade = update.message.text
    # можно вывести содержимое переменной grade, чтобы понять, что туда попало
    context.user_data['class'] = grade
    text = f'Я запомнил твой класс: {grade}'
    update.message.reply_text(text, reply_markup=ReplyKeyboardRemove())
    return ask_for_name(update, context)


def ask_for_name(update: Update, context: CallbackContext):
    text = [
        'Введи имя и фамилию.']
    text = '\n'.join(text)
    update.message.reply_text(text)
    return WAIT_FOR_NAME


def get_name(update: Update, context: CallbackContext):
    name = update.message.text
    # можно вывести содержимое переменной name, чтобы понять, что туда попало
    context.user_data['name'] = name
    text = f'Я запомнил твое имя и фамилию: {name}'
    update.message.reply_text(text)
    return ask_for_photo(update, context)



def ask_for_photo(update: Update, context: CallbackContext):
        text = [
            'Пришли мне свою фотографию, чтобы я убедился, что это ты).']
        text = '\n'.join(text)
        update.message.reply_text(text)
        return  WAIT_FOR_PHOTO

def get_photo(update: Update, context: CallbackContext):
        photo = update.message.text
        # можно вывести содержимое переменной name, чтобы понять, что туда попало
        context.user_data['photo'] = photo
        text = f'Поздравляю, ты зарегестрирован!'
        update.message.reply_text(text)
        return register_player(update, context)


def register_player(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    grade = context.user_data['class']
    name = context.user_data['name']
    photo = update.message.text

    write_to_db(user_id, grade, name, photo)

    # lines = ['Ты зарегестрирован!',
    #          f'Ты учишься в классе {grade}',
    #          f'Тебя зовут {name}']
    # text = '\n'.join(lines)
    # update.message.reply_text(text)

    return ConversationHandler.END

if __name__ == '__main__':
    main()


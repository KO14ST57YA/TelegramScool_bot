from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, ParseMode
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import CallbackContext
from Key import TOKEN



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
    dispetcher.add_handler(
         MessageHandler(Filters.text, do_keyboard)
     )

    # Бескончно просматривай обновления, пока работает код
    updater.start_polling()
    print(updater.bot.getMe)
    print('Бот запущен')
    updater.idle()


def do_start(update: Update, context: CallbackContext):
    text = 'Приветики, начнём?'
    update.message.reply_text(text)
    #do_keyboard(update, context)
    reply_keyboard(update, context)


def do_echo(update: Update, context: CallbackContext):
    text = update.message.text
    user_id = update.message.from_user.id
    name = update.message.from_user.name
    username = update.message.from_user.username

    lines = [
        f"Привет, {name}!",
        f"Твой {username=}.",
        f'Твой {user_id}.",'
        + text]
    lines_2 = [
        'html <b>жирный</b>',
        '<i>Курсив</i>',
        '<code>код</code>',
        '<s>перечеркнутый</s>',
        '<u>подчеркнутый</u>',
        '<pre language="c++">код</pre>',
        '<a href="1060.ru">Сайт школы</a>'
        ]
    text = '\n'.join(lines_2) #Перевод каждой строчки на новую
    update.message.reply_text(text, reply_markup=ReplyKeyboardRemove())
    update.message.reply_text(
        text,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True #Убрать предпросмотр ссылки
    )

    context.bot.send_message(user_id, text)

def do_keyboard(update: Update, context: CallbackContext): #Функция, которая создает клавиатуру
    buttons = [ # 3 ряда кнопок
        ['Один', 'Два'],
        ['Три', 'Четыри'],
        ['Пять']
    ]
    keyboard = ReplyKeyboardMarkup(buttons) # клавиатура класса ReplyKeyboardMarkup
    text = 'Выбери одну из операций на клавиатуре'
    update.message.reply_text(text, reply_markup=keyboard)

def reply_keyboard(update: Update, context: CallbackContext):
    button = [
        ['Yep', 'Nope']
    ]
    keyboard = ReplyKeyboardMarkup(button)
    text = 'Выбери одну из операций на клавиатуре'





if __name__ == '__main__': # Если файл запущен как главный, запусти файл main()
    main()

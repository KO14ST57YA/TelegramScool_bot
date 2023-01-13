from telegram.ext import Updater, CommandHandler


TOKEN = '5818310273:AAESvwTSH4Zfj8laHkNueVwbN67k-6bXHJ0'
def main():
     #
    updater = Updater(token=TOKEN)
     #Диспечер будет распределять события по обработчикам
    dispetcher = updater.dispatcher

     #Добавляем обработчик события из Telegram
    dispetcher.add_handler(
         CommandHandler('start', do_start)
    )

    updater.start_polling()
    updater.idle()


def do_start(update, context):
    text = 'Приветики, начнём?'
    update.message.reply_text(text)

if __name__ == 'Telegram bot_scool.py':
    Telegram bot_scool.py()

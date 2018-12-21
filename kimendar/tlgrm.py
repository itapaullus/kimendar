# Настройки
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
from kimendar import redmine
import os
bot_token = os.environ.get('TOKEN_TLG')
updater = Updater(token=bot_token) # Токен API к Telegram
dispatcher = updater.dispatcher
# Обработка команд
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hello Dear, lets talk')
    # bot.
    print('Start Command')

def testCommand(bot, update):
    try:
        bot.send_message(chat_id=update.message.chat_id,
                         text=redmine.get_support_info(),
                         parse_mode=telegram.ParseMode.HTML)
    except Exception as e:
        print(e)
    print('Test Command')

def textMessage(bot, update):
    response = 'Ok sweetty: ' + update.message.text
    print('inmessage: ' + update.message.text)
    bot.send_message(chat_id=update.message.chat_id, text=response)
# Хендлеры команд
start_command_handler = CommandHandler('start', startCommand)
test_command_handler = CommandHandler('test', testCommand)

# Хендлеры сообщений
text_message_handler = MessageHandler(Filters.text, textMessage)


# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
dispatcher.add_handler(test_command_handler)
# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()
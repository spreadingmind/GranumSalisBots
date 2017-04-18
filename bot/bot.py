from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import requests
import json

from local import TOKEN, ENDPOINT


CONFIRMATION_TEXT = "OK!"


def start(bot, update):
    update.message.reply_text('Hello World!')


def proceed(bot, update):
    # TODO: make async requests
    headers = {'content-type': 'application/json'}
    try:
        requests.post(ENDPOINT, data=json.dumps(update.to_dict()), headers=headers, timeout=5)
    except Exception as e:
        print(e)
    update.message.reply_text(CONFIRMATION_TEXT)


updater = Updater(TOKEN)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.all, proceed))


if __name__ == "__main__":
    updater.start_polling()
    updater.idle()

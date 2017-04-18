#!/usr/bin/env python3
import json

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

from local import TOKEN, ENDPOINT


def start(bot, update):
    proceed(bot, update)


def proceed(bot, update):
    # TODO: make async requests
    headers = {'content-type': 'application/json'}
    try:
        requests.post(ENDPOINT, data=json.dumps(update.to_dict()), headers=headers, timeout=5)
    except requests.HTTPError as e:
        print(e)

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.all, proceed))


if __name__ == "__main__":
    updater.start_polling()
    updater.idle()

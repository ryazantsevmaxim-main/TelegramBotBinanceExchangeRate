from functools import partial
from telegram.ext import CommandHandler, MessageHandler, Filters

from .commands import command_start
from .message import handler_message


def handlers(dispatcher, global_variables):
    # Command /start
    dispatcher.add_handler(CommandHandler('start', command_start))

    # Messages
    dispatcher.add_handler(MessageHandler(Filters.text, partial(handler_message, global_variables=global_variables)))


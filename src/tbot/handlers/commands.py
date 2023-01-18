import logging
from telegram import KeyboardButton, ReplyKeyboardMarkup, ParseMode


def command_start(update, context):
    """Displays a greeting"""
    chat = update.effective_chat
    user = update.message.from_user

    greeting = 'Hello'

    try:
        try:
            if user.last_name is not None:
                text = f'{greeting}, {user.last_name} {user.first_name}!'
            else:
                text = f'{greeting}, {user.first_name}!'
        except:
            if user.first_name is not None:
                text = f'{greeting}, {user.first_name}!'
            else:
                text = f'{greeting}!'
    except:
        text = f'{greeting}!'

    keyboard = [[KeyboardButton('Rate')]]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    context.bot.send_message(
        chat_id=chat.id,
        text=text,
        reply_markup=reply_markup,
        parse_mode=ParseMode.MARKDOWN
    )

    logging.info(f'Bot started by user {user.first_name} {user.last_name} (@{user.username})')


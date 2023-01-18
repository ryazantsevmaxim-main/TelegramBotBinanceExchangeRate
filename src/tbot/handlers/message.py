from src.tbot.parts import rate


def handler_message(update, context, global_variables):
    message = update.message.text

    # Menu
    if message == 'Rate':
        rate(update, context, global_variables)


def rate(update, context, global_variables):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"RUB -> USDT: {global_variables['rub_usdt']}\n"
             f"USDT -> THB: {global_variables['usdt_thb']}\n"
             f"RUB -> THB: {(round(global_variables['rub_usdt'] / global_variables['usdt_thb'], 4)) if (global_variables['rub_usdt'] != 0 and global_variables['usdt_thb'] != 0) else 0}\n\n "
             f"Last scrap: {global_variables['last_scrap']}"
    )

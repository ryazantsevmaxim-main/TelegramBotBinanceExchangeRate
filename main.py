# Python
import configparser
import logging
import time
from multiprocessing import Process, Manager
# Telegram
from telegram.ext import Updater
# Scraping
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# Project file
from src.tbot.handlers.handlers import handlers
from src.scraping import scraping_binance


def main():
    format_app = '%(asctime)s %(levelname)s: %(message)s'
    logging.basicConfig(filename='log.log', level=logging.INFO, format=format_app)

    manager = Manager()

    global_variables = {
        "was_first_scrap": False,
        "last_scrap": "",
        "rub_usdt": 0,
        "usdt_thb": 0,
    }

    global_variables = manager.dict(global_variables)

    process_tbot = Process(target=tbot, args=(global_variables,))
    process_scraping = Process(target=scraping, args=(global_variables,))

    process_tbot.start()
    process_scraping.start()

    process_tbot.join()
    process_scraping.join()


def tbot(global_variables):
    """Telegram bot"""
    print('The bot is launched. Click Ctrl+C to stop')

    try:
        logging.info("Start bot")

        # Token from BotFather
        config = configparser.ConfigParser()
        config.read("config.ini")
        token = config['Telegram']['token']

        # Create Updater
        updater = Updater(token)

        # Get Dispatcher for creating handlers
        dispatcher = updater.dispatcher

        # Create handlers
        handlers(dispatcher, global_variables)

        # Launch of listening messages
        updater.start_polling()

        # The handler of Ctrl+C
        updater.idle()

    except Exception as e:
        logging.error(e)


# Scraping Binance
def scraping(global_variables):
    try:
        logging.info("Start scraping")

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        service = Service(ChromeDriverManager().install())

        while True:
            scraping_binance(global_variables, service, options)

            if global_variables["was_first_scrap"]:
                time.sleep(300)

    except Exception as e:
        logging.error(e)
        scraping(global_variables)

if __name__ == '__main__':
    main()


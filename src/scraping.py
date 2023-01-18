import logging
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By


def scraping_binance(global_variables, service, options):
    # Chrome manager
    driver = webdriver.Chrome(service=service, options=options)
    logging.info("Open driver")
    driver.implicitly_wait(30)
    driver.delete_all_cookies()

    # RUB -> USDT
    driver.get('https://p2p.binance.com/en/trade/TinkoffNew/USDT?fiat=RUB')
    driver.get('https://p2p.binance.com/en/trade/TinkoffNew/USDT?fiat=RUB')
    driver.refresh()
    driver.get('https://p2p.binance.com/en/trade/TinkoffNew/USDT?fiat=RUB')

    # Find string
    try:
        rate_rub_usdt = float(
            (driver.find_elements(By.CSS_SELECTOR, "div[data-tutorial-id='trade_price_limit'] "))[0].text.split('\n',
                                                                                                                1)[0])

        global_variables['rub_usdt'] = rate_rub_usdt
    except Exception as e:
        logging.error(e)

    # USDT -> THB
    driver.get('https://p2p.binance.com/en/trade/sell/USDT?fiat=THB&payment=BANK')
    driver.refresh()
    driver.get('https://p2p.binance.com/en/trade/sell/USDT?fiat=THB&payment=BANK')

    # Find string
    try:
        rate_usdt_thb = float(
            (driver.find_elements(By.CSS_SELECTOR, "div[data-tutorial-id='trade_price_limit'] "))[0].text.split('\n',
                                                                                                                1)[0])

        global_variables['usdt_thb'] = rate_usdt_thb
    except Exception as e:
        logging.error(e)

    # Closing the driver
    driver.close()

    if global_variables["rub_usdt"] != 0 and global_variables["usdt_thb"] != 0:
        global_variables["last_scrap"] = (datetime.now() + timedelta(hours=7)).strftime("%m/%d/%Y, %H:%M")

        if not global_variables["was_first_scrap"]:
            global_variables["was_first_scrap"] = True
            logging.info("Was first scrap")

    logging.info(f'rub_usdt: {global_variables["rub_usdt"]}, '
                 f'usdt_thb: {global_variables["usdt_thb"]}, '
                 f'last_scrap: {global_variables["last_scrap"]}')


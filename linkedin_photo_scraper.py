import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

logging.basicConfig(filename='out.log', level=logging.INFO)


def login(driver, email, password):
    try:
        logging.info('Logging into LinkedIn')
        driver.get('https://www.linkedin.com/login')
        time.sleep(2)

        email_input = driver.find_element(By.ID, 'username')
        email_input.send_keys(email)

        password_input = driver.find_element(By.ID, 'password')
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)

        logging.info('Successfully logged into LinkedIn')
        time.sleep(3)
    except Exception as e:
        logging.error(f"Login failed: {e}")

# def photo_scrape(driver, profile):
#     try:
#         logging.info('Scraping profile photo')
#         driver.get(profile)
#         time.sleep(2)

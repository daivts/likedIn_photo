import logging

from selenium import webdriver

from linkedin_photo_scraper import login

logging.basicConfig(filename='out.log', level=logging.INFO)


def test_login_with_real_driver():
    driver = webdriver.Chrome()
    try:
        login(driver, "wopavir584@aleitar.com", "daivts1488")
    finally:
        driver.quit()

from selenium import webdriver
# noinspection PyUnresolvedReferences
from user_account import USER_NAME, PASSWORD
from exception import LoginError, IncorrectAccountError
from constant import CHROME_DRIVER_PATH, LOGIN_PATH, EXPECTED_PATH, EMAIL_ID, PASSWORD_ID, LOGIN_BUTTON_ID
import time
from cryptography.fernet import Fernet

try:
    print('[INFO]Logging in')
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(CHROME_DRIVER_PATH, options=options)
    browser.get(LOGIN_PATH)
    browser.find_element_by_id(EMAIL_ID).send_keys(USER_NAME)
    browser.find_element_by_id(PASSWORD_ID).send_keys(PASSWORD)
    browser.find_element_by_id(LOGIN_BUTTON_ID).click()
    time.sleep(5)
    if browser.current_url != EXPECTED_PATH:
        raise IncorrectAccountError
    print('[INFO]Finish logging in')
except LoginError:
    print('[ERROR]Error happened while logging in')
    raise LoginError
except IncorrectAccountError:
    print('[ERROR]Your account is not existed')
finally:
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    USER_NAME = cipher_suite.encrypt(USER_NAME.encode())
    PASSWORD = cipher_suite.encrypt(PASSWORD.encode())

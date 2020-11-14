from selenium import webdriver
import exceptions as ex
import constants as cons
import time
import sys


if __name__ == '__main__':
    try:
        print('[INFO]Please enter your facebook account')
        user_name = input('Your user name: ')
        password = input('Your password: ')
        print('[INFO]Logging in')
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        browser = webdriver.Chrome(cons.CHROME_DRIVER_PATH, options=options)
        browser.get(cons.FACEBOOK_LOGIN_PATH)
        browser.find_element_by_id(cons.EMAIL_ID).send_keys(user_name)
        browser.find_element_by_id(cons.PASSWORD_ID).send_keys(password)
        browser.find_element_by_id(cons.LOGIN_BUTTON_ID).click()
        time.sleep(5)
        if browser.current_url != cons.EXPECTED_PATH:
            raise ex.IncorrectAccountError
        print('[INFO]Finish logging in')
    except ex.LoginError:
        print('[ERROR]Error happened while logging in')
        raise ex.LoginError
    except ex.IncorrectAccountError:
        print('[ERROR]Your account is not existed')

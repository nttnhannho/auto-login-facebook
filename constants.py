import os


# Download your chromedriver version from https://chromedriver.chromium.org/downloads
CHROME_FILE_NAME = 'chromedriver.exe'
CHROME_FOLDER = 'chromedriver'
CURRENT_WORKING_PATH = os.getcwd()
CHROME_DRIVER_PATH = os.path.join(CURRENT_WORKING_PATH, CHROME_FOLDER, CHROME_FILE_NAME)
FACEBOOK_LOGIN_PATH = r'https://www.facebook.com/login'
EXPECTED_PATH = r'https://www.facebook.com/'
EMAIL_ID = 'email'
PASSWORD_ID = 'pass'
LOGIN_BUTTON_ID = 'loginbutton'

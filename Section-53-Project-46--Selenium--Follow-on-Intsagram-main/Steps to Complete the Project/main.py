from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
from selenium.webdriver.common.by import By
# TODO 1 - Get your chrome driver location and instagram credentials
CHROME_DRIVER_PATH = ""
SIMILAR_ACCOUNT = ""
USERNAME = ""
PASSWORD = ""

# TODO 2 - Create class with login, find followers and follow

class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(4)

        username = self.driver.find_element(by=By.NAME, value="username")
        password = self.driver.find_element(by=By.NAME, value="password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(3)
        password.send_keys(Keys.ENTER)

    # TODO 3 - Find followers of similar page
    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element(by=By.XPATH, value="//div[text()=' followers']")
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element(by=By.XPATH, value='/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    # TODO 4 - Follow all followers
    def follow(self):
        all_buttons = self.driver.find_element(by=By.CSS_SELECTOR, value="li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value='/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()

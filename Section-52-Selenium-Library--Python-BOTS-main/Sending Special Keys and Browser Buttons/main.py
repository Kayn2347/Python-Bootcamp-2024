from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import
import time


chrome_diver_path = "/Users/Acer/Python For Everyone/chromedriver"
service = ChromeService(executable_path=chrome_diver_path)
new_driver = webdriver.Chrome(service=service)
new_driver.get("https://stackoverflow.com/?tab=hot")
search = new_driver.find_element(by=By.NAME, value="q")
search.is_enabled()
print(search.is_enabled())
new_driver.quit()

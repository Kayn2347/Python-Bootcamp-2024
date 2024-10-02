from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_diver_path = "/Users/Acer/Python For Everyone/chromedriver"
service = ChromeService(executable_path=chrome_diver_path)
new_driver = webdriver.Chrome(service=service)
new_driver.get("https://forms.gle/uWU2jkbBLy6SuzfTA")
time.sleep(5)
my_details = ["Kayn", "Lourence", "kaynlourence1210@gmail.com"]
text_boxes = new_driver.find_elements(by=By.CLASS_NAME, value="whsOnd zHQkBf")
for i in range(len(text_boxes)):
    text_boxes[i].send_keys(my_details[i])

submit = new_driver.find_element(by=By.CLASS_NAME, value="NPEfkd.RveJvd.SnByac")
submit.click()
# players = new_driver.find_elements(by=By.CLASS_NAME, value="name")
# salaries = new_driver.find_elements(by=By.Class_NAME, value="hh-salaries-sorted"
# salaries_dict = {}
# for i in range(len(salaries))
#     salaries_dict[i] ={
#         "name": player[i.] text,
#         "amount": salaries[i].text
# }
  
# print(salaries_dict)
# faceboo_share = new.driver.find_element(by=By.ID, value="share-facebook")
# facebook_share.click()

# Click buttons
# search = new_driver.find_element(by=By.CLASS_NAME, value="branding__search-form")
# search.click()
# search_bar = new_driver.find_element(by=By.NAME, value="s")
# search_bar.send_keys("John Wall")
# search_bar.send_keys(Keys.ENTER)





new_driver.close()


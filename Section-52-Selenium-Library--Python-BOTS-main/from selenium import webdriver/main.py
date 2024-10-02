from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import pprint


chrome_diver_path = "/Users/Acer/Python For Everyone/chromedriver"
service = ChromeService(executable_path=chrome_diver_path)
new_driver = webdriver.Chrome(service=service)
new_driver.get("https://hoopshype.com/salaries/players/")
players = new_driver.find_elements(by=By.CLASS_NAME, value="name")
salaries = new_driver.find_elements(by=By.Class_NAME, value="hh-salaries-sorted"
salaries_dict = {}
for i in range(len(salaries))
    salaries_dict[i] ={
        "name": player[i.] text,
        "amount": salaries[i].text
    }
  

print(salaries_dict)


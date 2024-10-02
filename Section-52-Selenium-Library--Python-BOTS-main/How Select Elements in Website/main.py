from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

# for windows
chrome_driver_path = "C:\Python for Everyone\chromediver_win32\chromedriver.exe"
service = ChromeService(execute_path=chrome_driver_path)
new_driver = webdriver.Chrome(service=service)
new_driver.get("https://stockoverflow.com/?tab=hot")
title = new_driver.find_element(by=By.Class_Name, value="s-post-summary--content-title")
print(title.text)

from selenium import webdriver

# for windows
# chrome_driver_path = "C:\Python for Everyone\chromediver_win32\chromedriver.exe"

 chrome_driver_path = "/Users/Acer/Python for Everyone/chromedriver"
new_driver = webdriver.Chrome(chrome_driver_path)
new_driver.get("https://www.google.com")
new_driver.quit()

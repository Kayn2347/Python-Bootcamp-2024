import pyautogui
import time
import random


def looking_busy():
    while True:
        random_x = random.randint(-10, 10)  # you can set bigger number to see movement
        random_y = random.randint(-10, 10)  # you can set bigger number to see movement
        pyautogui.moveRel(random_x, random_y)
        time.sleep(5)


looking_busy()

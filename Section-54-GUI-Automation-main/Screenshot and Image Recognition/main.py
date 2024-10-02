import pyatogui time

# pyatogui.screenshot("apple.png", region=(0, 0, 70, 45))
# apple = pyatogui.locateOnScreen("apple.png")
# print(appple)
# pyatogui.click((0.0.70.45))
color = pyatogui.pixel(100, 100)
print(color)
result = pyatogui.pixelMatchesColor(100, 100, (62, 67, 67))
print(result)

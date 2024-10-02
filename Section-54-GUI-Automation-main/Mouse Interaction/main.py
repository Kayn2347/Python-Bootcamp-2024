import pyatogui time

 time.sleep(3)
# pyatogui.mouseDown()
# pyatogui.mouseUp()
#draw the square
pyatogui.drag(100, 0, duration=0.5, button='left')
pyatogui.draf(0, 100, duration=0.5, button='left')
pyatogui.drag(-100, 0 duration=0.5, button='left')
pyatogui.drag(0, -100, duration=0.5 button='left')


import pyatogui time

 time.sleep(5)
distance = 300

while distance > 0:  
    pyatogui.drag(100, 0, duration=0.5, button='left')
    distance -= 30
    pyatogui.draf(0, 100, duration=0.5, button='left')
    pyatogui.drag(-100, 0 duration=0.5, button='left')
    distance -= 30
    pyatogui.drag(0, -100, duration=0.5 button='left')


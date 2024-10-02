import pyautogui, time

form_data = [{'name': 'Alice', 'position': 'Python Developer', 'language': 'Python', 'agree_disagree': 4,
              'comments': 'I Love Python.'},
             {'name': 'John', 'position': 'IT Analyst', 'language': 'Swift', 'agree_disagree': 4, 'comments': 'n/a'},
             {'name': 'Edy', 'position': 'Project Manager', 'language': 'Java', 'agree_disagree': 1,
              'comments': 'I prefer Java over Python'},
             {'name': 'Redy', 'position': 'QA Tester', 'language': 'Python', 'agree_disagree': 5,
              'comments': 'Python is the best'},
             ]

pyautogui.PAUSE = 0.5
print('Ensure that the browser window is active and the form is loaded!')

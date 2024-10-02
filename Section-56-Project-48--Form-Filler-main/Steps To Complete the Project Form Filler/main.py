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

for person in form_data:
    # Give the user a chance to stop the script using CTRL+C
    print('--- 5 Seconds PAUSE to stop the script- PRESS CTRL+CC ---')
    time.sleep(5)
    pyautogui.write(['\t', '\t'])
    print(f"Entering {person['name']} info...")
    # Fill out Name field
    pyautogui.write(person['name'] + '\t')
    # Fill out position field
    pyautogui.write(person['position'] + '\t')

    # Fill out language field
    if person['language'] == 'Python':
        pyautogui.write(['space', '\t', '\t'], 0.5)
    elif person['language'] == 'Java':
        pyautogui.write(['down', '\t', '\t'], 0.5)
    elif person['language'] == 'Javascript':
        pyautogui.write(['down', 'down', '\t', '\t'], 0.5)
    elif person['language'] == 'Swift':
        pyautogui.write(['down', 'down', 'down', '\t', '\t'], 0.5)

    # Fill out agree disagree field
    if person['agree_disagree'] == 1:
        pyautogui.write(['space', '\t', '\t'], 0.5)
    elif person['agree_disagree'] == 2:
        pyautogui.write(['right', '\t', '\t'], 0.5)
    elif person['agree_disagree'] == 3:
        pyautogui.write(['right', 'right', '\t', '\t'], 0.5)
    elif person['agree_disagree'] == 4:
        pyautogui.write(['right', 'right', 'right', '\t', '\t'], 0.5)
    elif person['agree_disagree'] == 5:
        pyautogui.write(['right', 'right', 'right', 'right', '\t', '\t'], 0.5)

    # Fill out Additional comments
    pyautogui.write(person['comments'])
    pyautogui.press('\t')

    # "Click" Submit button by pressing Enter.
    time.sleep(2)
    pyautogui.press('enter')

    # Wait until form page has loaded.
    print('Submitted form.')
    time.sleep(5)

    # "Click" the "Submit another response" link
    pyautogui.write(['\t', '\n'])

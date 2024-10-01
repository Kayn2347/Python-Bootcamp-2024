import re

def find_three_con(text):
    mo = re.search('\d\d\d', text)
    if mo == None:
        return 'Not found'
    else:
        return mo.group()

text = "My phone number is: 234-456-8765"  

print(find_three_con(text))  
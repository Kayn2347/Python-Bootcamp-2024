import re, data

def extract_email(text):
    regex = re.compile(r'\[a-z]+@\w+\.com')
    mo = regex.findall(text)
    return mo

print(extract_email(data.text))

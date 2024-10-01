import re

def text_match(text):
    capital_regex = re.compile('^[A-Z]+_[A-Z]+$')
    mo = capital_regex.search(text)
    if mo:
        return 'Matched'
    else:
        return 'Not matched'

print(text_match('BB_CCAA'))
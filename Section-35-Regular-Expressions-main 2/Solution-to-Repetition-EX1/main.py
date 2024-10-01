import re
def text_match(text):
        regex_pattern = re.compile(r'AB*')
        mo = regex_pattern.search(text)
        if mo == None:
            return('Not matched')       
        else:
            return 'Matched'

print(text_match("A"))
print(text_match("ABC"))
print(text_match("ABBC"))
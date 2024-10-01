import re

phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_regex.search('555-666-8888')


regex = re.compile(r'\S')
mo = regex.findall('foo bar\n\t')

text = '''The use of 1234 to say "I love you" comes from the following idea: I have 1 thing 2 say: 3 words 4 you'''

regex = re.compile(r'\d+\s\w')
mo = regex.findall(text)
print(mo)
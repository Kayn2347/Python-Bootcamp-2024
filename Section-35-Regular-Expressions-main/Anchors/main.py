import re
# ^ and \A
text = "foo\nbar\nbaz"
regex = re.compile(r'bar\Z', re.M)
mo = regex.search(text)

# \B

regex = re.compile(r'\Bfoo\B')
mo = regex.search('barfoobaz')
print(mo)
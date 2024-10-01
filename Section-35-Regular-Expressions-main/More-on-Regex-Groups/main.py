import re

regex = re.compile(r'(\w+),(?:\w+),(\w+)')
mo = regex.search("foo,qux,bar")
print(mo.group(1,2))

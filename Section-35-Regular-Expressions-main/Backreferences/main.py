import re

regex = re.compile(r'(\w+),\1')
mo = regex.search('like,like')
print(mo)
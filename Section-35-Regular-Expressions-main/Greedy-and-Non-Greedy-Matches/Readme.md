import re

phone_regex = re.compile('\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_regex.search('555-666-8888')

phone_regex = re.compile(r'0|1|2|3|4|5|6|7|9')
mo = phone_regex.search('555-666-8888')
print(mo)


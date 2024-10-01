import re

consonant_regex = re.compile(r'[^0-9]')

mo = consonant_regex.findall('1234five^')
print(mo)


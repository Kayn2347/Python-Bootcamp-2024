import re


for i in re.finditer(r'(\w+)', ',,..foo...bar...baz'):
    print(i)
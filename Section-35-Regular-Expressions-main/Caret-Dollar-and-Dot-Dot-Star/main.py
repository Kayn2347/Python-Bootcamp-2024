import re

begin_hello_regex = re.compile(r'world')
mo = begin_hello_regex.search('Hello world. Welcome world')
# print(mo)

# using ^ and $ together
all_digits_regex = re.compile(r'^\d+$')
mo = all_digits_regex.search('4738465839848484848')
# print(mo)


# using dot (.)

regex = re.compile(r'.{1,5}ad')
mo = regex.findall('The love you download still is equal to the love you upload')
# print(mo)


#using dot star .*
text = "Make: BMW Model: X5"
car_regex = re.compile(r'Make: (.*) Model: (.*)')
mo = car_regex.findall(text)
# print(mo)


# .* greedy and non greedy
text = '<Hello world> Welcome!>'
regex = re.compile(r'<(.*)>')
mo = regex.search(text)
# print(mo)

# .* new line
new_text = "I love Python.\nI enjoy learning it using online Python for Everyone course"
regex = re.compile(r'.*',re.DOTALL)
mo = regex.search(new_text)
#print(new_text)

#ignore case sensitive
vowel_regex = re.compile(r'[aeiou]', re.I)
mo = vowel_regex.findall('I love Python')
# print(mo)

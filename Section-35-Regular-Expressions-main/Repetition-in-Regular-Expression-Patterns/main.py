import re

iron_regex = re.compile(r'Iron(wo)?man')
mo = iron_regex.search("The adventures of Ironwowowoman")
# print(mo)

phone_regex= re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_regex.search("This is my phone number: 555-777-8888")


quest_regex = re.compile(r'drink?')
mo = quest_regex.search("Do you want to drink")

# Star Metacha *

regex = re.compile(r'foo-bar')
mo = regex.search("foo--bar")

iron_regex = re.compile(r'Iron(wo)*man')
mo = iron_regex.search("The adventures of Ironwowowoman")

quest_regex = re.compile(r'drink*')
mo = quest_regex.search("Do you want to drink*")


# Plus Metacharacter +
regex = re.compile(r'foo-+bar')
mo = regex.search("foo-bar")


iron_regex = re.compile(r'Iron(wo)?man')
mo = iron_regex.search("The adventures of Ironwowowoman")

regex = re.compile(r'(\+\?\*)+')
mo = regex.search("I have learnt about +?*+?*+?*+?*+?* regen syntax")


# Using Curly Braces

regex = re.compile(r'foo-{,}bar')
mo = regex.search("foo---------bar")


phone_regex= re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo = phone_regex.search("This is my phone number: 555-777-8888,666-444-3333,111-222-3333")

print(mo)
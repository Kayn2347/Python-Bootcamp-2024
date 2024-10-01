# Groups ()
#  555-444-7777

# import re

# phone_num_regex = re.compile(r'\d\d\d-(\d\d\d-\d\d\d\d)')
# mo = phone_num_regex.search("This is my number: 555-444-7777")
# print(mo.group(0))

# #(555) 666-777

# phone_num_regex = re.compile(r'\(\d\d\d\) (\d\d\d-\d\d\d\d)')
# mo = phone_num_regex.search("This is my number: (555) 444-7777")
# print(mo.group(1))


#Pipe character

dis_regex = re.compile(r'dis(agree|allow|array|connect)')
text = "I like Python"
print(dis_regex.search(text))
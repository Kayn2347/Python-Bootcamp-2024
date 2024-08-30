my_string = "I_love_learning_Python"
output = my_string.split("_", maxsplit = 3)
print(output)
join_back = " ".join(output)
print(join_back)


import string

str1 = "/*kayn is @developer & musician"
print("Original string is ", str1)

# use translate function of a string
# and maketrans function of str class
new_str = str1.translate(str.maketrans('', '', string.punctuation))

print("New string is ", new_str)
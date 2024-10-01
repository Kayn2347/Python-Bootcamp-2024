import re


def find_words(text):
    regex = re.compile(r'\b\w{3,5}\b')
    result_list = regex.findall(text)
    return result_list

print(find_words("I like Python for Everyone course. It is the best one out there."))

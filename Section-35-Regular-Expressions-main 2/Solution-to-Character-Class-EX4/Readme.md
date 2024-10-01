import re

def start_ae(text):
    ae_regex = re.compile('[ae]\w+')
    mo = ae_regex.findall(text)
    return mo

text = "The following example creates a list with 50 elements. All elements are then added to the list when the list is created."

print(start_ae(text))

#555-444-8888
def is_phone_number(p_string):
    if len(p_string) != 12:
        #Not phone number size
        return False
    for i in range(0,3):
        if not p_string[i].isdecimal():
            # area code is missing
            return False
    if p_string[3] != '-':
        # missing first dash
        return False
    for i in range(4,7):
        if not p_string[i].isdecimal():
            # missing first digits
            return False
    if p_string[7] != '-':
        # missing second dash
        return False
    for i in range(8,12):
        if not p_string[i].isdecimal():
            #last digits missing
            return False
    return True

print(is_phone_number("123-123-8888"))
text = "This is my number: 555-333-4444 and the office is: 666-777-8888"
is_pnumber = False
for i in range(len(text)):
    text_piece = text[i:i+12]
    if is_phone_number(text_piece):
        print(f"Phone number is found: {text_piece}")
        is_pnumber = True
if not is_pnumber:
    print("There is not any number")

# Using Regular expression
print()
import re

mo = re.findall('\d\d\d-\d\d\d-\d\d\d\d', text)
print(mo)
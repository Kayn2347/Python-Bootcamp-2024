import re
from data import text


# TODO 1 - Create Regex for Phone Number
# 333-0000, 314-444-1223, (425) 456-2323, 111-0000 ext 12345, ext. 67883, x1274
phone_regex = re.compile(r'''(
                         ((\d\d\d)|(\(\d\d\d\)))?  # Area code (optional)
                         (\s|-)?                    # First separator
                         \d\d\d                     # First three digits
                         -                          # Separator
                         \d\d\d\d                   # Last Four digits
                         (\s((ext(\.)?\s)|x)(\d{2,5}))?
                         )
                         ''', re.VERBOSE)
# print(phone_regex.search('(807) 888-0000 x345'))

# TODO 2 - Create Regex for Email
# some.+_thing@appmillers.com
email_regex = re.compile('''
                         [a-zA-z_.+]+   # Name Part
                         @              # @ symbol
                         [a-zA-Z_.+]+   # domain part
                         ''', re.VERBOSE)

# TODO 3 - Extract phone number or email from text
extracted_phone_number = phone_regex.findall(text)
# print(extracted_phone_number)
all_phone_numbers = []
for phone_number in extracted_phone_number:
    all_phone_numbers.append(phone_number[0])

extracted_emails = email_regex.findall(text)


# TODO 4 - Print phone numbers and emails each on new line.
results = '\n'.join(all_phone_numbers) + '\n'.join(extracted_emails)
print(results)


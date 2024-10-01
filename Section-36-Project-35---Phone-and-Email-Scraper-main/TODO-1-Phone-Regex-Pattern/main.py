import re
from data import text


# TODO 1 - Create Regex for Phone Number
# 333-0000, 314-444-1223, (425) 456-2323, 111-0000 ext 12345, ext. 67883, x1274
phone_regex = re.compile(r'''
                         ((\d\d\d)|(\(\d\d\d\)))?  # Area code (optional)
                         (\s|-)?                    # First separator
                         \d\d\d                     # First three digits
                         -                          # Separator
                         \d\d\d\d                   # Last Four digits
                         (\s((ext(\.)?\s)|x)(\d{2,5}))?
                         ''', re.VERBOSE)
print(phone_regex.search('(807) 888-0000 x345'))

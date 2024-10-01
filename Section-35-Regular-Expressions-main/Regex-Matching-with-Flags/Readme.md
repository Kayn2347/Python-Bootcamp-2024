import re

# Verbose
regex_phone = r'''^             # Start of string
                (\(\d{3}\))?    # Optional are code
                \s*             # Optional whitespace
                \d{3}           # Three digit prefix
                [-.]            # Separator character
                \d{4}           # Four digit line number
                $               # Anchor for end of string
                '''         
mo = re.search(regex_phone, '(123) 313-7878', re.VERBOSE)
print(mo)
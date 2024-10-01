import re
def is_decimal(num):
    regex = re.compile(r'^[0-9]+(\.[0-9]{1,2})?$')
    result = regex.search(num)
    return bool(result)

print(is_decimal('123.11'))
print(is_decimal('123.1'))
print(is_decimal('123.123'))

import re

def f(match_obj):
    s =match_obj.group(0)
    if s.isdigit():
        return str(int(s) * 10)
    else:
        return s.upper()

result_string = re.sub(r'\w+', 'xxx', 'foo.bar.qux.baz', count=2)
print(result_string)
import re

def text_match(text):
        regex = re.compile(r'c.+e$', re.I)
        text_list = text.split()
        result = []
        for i in text_list:
            mo = regex.findall(i)
            result.extend(mo)
        return result

text = 'I come to CTRE every'
print(text_match(text))

print(re.findall(r"\bc\w*?e\b",text,re.I)) #using boundary

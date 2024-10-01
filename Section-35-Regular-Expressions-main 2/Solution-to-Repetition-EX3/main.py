import re
def text_match(text):
        regex_pattern = re.compile(r'((l|L)ove(rs)?)')
        mo = regex_pattern.findall(text)
        count = len(mo)
        return count


text = '''Lovers in love
Lovers in love
Love, love, love, love, love
Love, love, love, love, love
Love, love, love, love, love
Love, love, love, love, love
Lovers loving love just like these lovers are loving love in love
Lovers loving love just like these lovers are loving love in love'''

print(text_match(text))

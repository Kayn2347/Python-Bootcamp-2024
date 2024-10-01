import re

def remove_zero(ip):
    output = re.sub('\.[0]*', '.', ip)
    return output

print(remove_zero("211.07.095.122"))
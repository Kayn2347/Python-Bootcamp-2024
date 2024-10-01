import re

str='''What’s New In Python 3.10
Release 3.10.1
Date January 10, 2022
Editor Pablo Galindo Salgado
This article explains the new features in Python 3.10, compared to 3.9.'''

#Type your answer here.

regex=regex = r'3\S+'
data=re.findall(regex, str)

print(data)
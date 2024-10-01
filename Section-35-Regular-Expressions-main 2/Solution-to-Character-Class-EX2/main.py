import re
def extract_date(url):
       regex = re.compile(r'(\d{4})/(\d{1,2})/(\d){1,2}')

       mo = regex.findall(url)
       return mo
url1= "https://www.apmillers.com/news/daily/wp/2024/17/09/regular-expressions-patterns/"

               
print(extract_date(url1))
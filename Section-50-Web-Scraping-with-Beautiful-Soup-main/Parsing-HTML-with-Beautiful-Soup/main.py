from bs4 import BeautifulSoup
import lxml

with open("home.html") as file:
  content = file.read()

new_soup = BeautifulSoup(content, "html.parser")
print(new_soup.prettify())
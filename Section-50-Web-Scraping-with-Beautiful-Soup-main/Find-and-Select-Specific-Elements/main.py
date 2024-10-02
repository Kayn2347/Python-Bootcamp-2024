from bs4 import BeautifulSoup
import lxml

with open("home.html") as file:
  content = file.read()

# new_soup = BeautifulSoup(content, "html.parser")
# anchor_tags = new_soup.find_all(name="a")
# for tag in anchor_tags:
#   # print(tag.getText())
#   print(tag.get("href"))

# new_soup = BeautifulSoup(content, "html.parser")
# h1 = new_soup.find_all(name="h1", id="name")
# for header in h1:
#   print(header.getText())


# new_soup = BeautifulSoup(content, "html.parser")
# h3 = new_soup.find_all(name="h3", class_="heading")
# for header in h3:
#     print(header.getText())

# new_soup = BeautifulSoup(content, "html.parser")
# anchors = new_soup.find_all(name="a")
# print(anchors[1])
# # for anchor in anchors:
# #     print(anchors.get("href"))

# new_soup = BeautifulSoup(content, "html.parser")
# appmillers_url = new_soup.select_one(selector="p a")
# print(appmillers_url.get("href"))

new_soup = BeautifulSoup(content, "html.parser")
tag = new_soup.select_one(selector="heading")
print(tag)
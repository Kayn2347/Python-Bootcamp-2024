import requests
from bs4 import BeautifulSoup


url = "https://stackoverflow.com/?tab=hot"
response = requests.get(url)
stackoverflow = response.text

new_soup = BeautifulSoup(stackoverflow, "html.parser")
questions = new_soup.find_all(name="h3", class_="s-post-summary--content-title")
question_titles = []
question_links = []
for question_tag in questions:
    question_title = question_tag.getText().strip()
    question_titles.append(question_title)
    question_link = "www.stackoverflow.com"+question_tag.find(name="a").get("href")
    question_links.append(question_link)
votes = []

question_votes = new_soup.find_all(name="div", class_="s-post-summary--stats-item s-post-summary--stats-item__emphasized")
for question_vote in question_votes:
    votes.append(question_vote.getText())

largest_vote = max(votes)
index = votes.index(largest_vote)
print(question_titles[index])
print(question_links[index])


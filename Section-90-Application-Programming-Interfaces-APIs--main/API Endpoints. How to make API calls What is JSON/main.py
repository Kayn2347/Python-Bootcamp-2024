import requests

reponse = requests.get("https://official-joke-api.appspot.com/random_joke")
print(response.content)

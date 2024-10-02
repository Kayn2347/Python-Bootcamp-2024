import requests

reponse = requests.get("https://official-joke-api.appspot.com/random_joke")
response.raise_for_status()
#print(response.json())
print(response.json()['setup'])
print(response.json()['punchline'])

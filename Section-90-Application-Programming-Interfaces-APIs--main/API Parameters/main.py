import requests

# reponse = requests.get("https://official-joke-api.appspot.com/random_joke")
# response.raise_for_status()
# #print(response.json())
# print(response.json()['setup'])
# print(response.json()['punchline'])
parameters = {
     'lat': 48.856613 ,
     'lng': 2.352222,
}
response = request.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data['results']['sunrise'])
print(data['results']['sunset'])

import requests
import os


# api_key = "a593af561aaa47065522a1250ea4cc3"
api_key = os.environ.get("own_api_key")
print(api_key)
endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_params = {
    "q": "Paris",
    "appid": api_key
}
response = requests.get(endpoint, params=api_params)
print(response.json())

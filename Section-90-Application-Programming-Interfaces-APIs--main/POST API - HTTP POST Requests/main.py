import requests


url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": 'Sample Title',
    "body": 'We are testing Post request',
    "userId": 1,
}

response = requests.post(url, json=data)
print(response)
if response.status_code == 201:
    print("Success")
else:
     print("Failed")

print(response.content)

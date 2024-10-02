import requests


#Put method
# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "id": 1,
#     "title": 'foo',
#     "body": 'bar',
#     "userId": 1,
# }

# # response = requests.post(url, json=data)
# response = requests.put(url, data)
# print(response.json())

# url = "https://jsonplaceholder.typicode.com/posts"


#Delete method
data = {
  "body": 'bar',
}


# response = requests.post(url, json=data)
response = requests.delete(url, data)
print(response.status_code())

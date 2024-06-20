import requests

url = "https://httpbin.org/post"

input = {"k1": "v1", "k2": "v2", "k3": "v3"}

response = requests.post(url, data=input)

print(response.headers)
print(response.json())

from requests import HTTPError
import requests

url = "https://httpbin.org/post"
input = {"k1": "v1", "k2": "v2", "k3": "v3"}

filename = "test.txt"

upl_file = open(filename, "rb")

# response = requests.post(url, data=input)
# response = requests.post(url, json=input)
# response = requests.post(upl_file, files={"file:": upl_file})

response = requests.post(url, files={"file": upl_file})
    

print(response)
print("\n")
print(response.headers)
print("\n")
print(response.json())

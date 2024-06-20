import requests

response = requests.get("https://api.github.com/")
print(response)

print(response.status_code)

if response.status_code == 200:
    print("Successful Request")
elif response.status_code == 404:
    print("Resource Not Found")
else:
    print("Other Status Code")


if response:
    print("Successful Request")
else:
    print("Error with Request")

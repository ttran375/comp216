import requests
from requests.exceptions import HTTPError

# response = requests.get("https://api.github.com/")
# print(response)

urls = [
    "https://api.github.com/",
    "https://api1.github.com/",
    "https://api.github.com/events",
]

for url in urls:
    try:
        response = requests.get(url)
        # print(response)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP Error - {http_err}")
    except Exception as err:
        print("Error")
    else:
        print("Successful!")

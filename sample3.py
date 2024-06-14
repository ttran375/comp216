from requests import HTTPError
import requests

url = "https://api.github.com/"

try:
    response = requests.get(url)
    # print(response)
    response.raise_for_status()
except HTTPError as http_err:
    print(f"HTTP Error - {http_err}")
except Exception as err:
    print("Error")
else:
    # print("Success!")
    # cont = response.content
    # print(type(cont))
    # print(cont)

    response.encoding = "utf-8"
    cont_text = response.text

    print(type(cont_text))
    print(cont_text)

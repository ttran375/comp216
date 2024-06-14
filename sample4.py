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
    header = response.headers
    print(type(header))

    print(header)

    date = header["Date"]
    print(date)
    cont_type_1 = header["Content-Type"]
    cont_type_2 = header["content-type"]
    print(cont_type_1, cont_type_2)

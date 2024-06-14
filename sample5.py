from requests import HTTPError
import requests

url = "https://api.github.com/events"

try:
    response = requests.get(url, stream=True)
    # print(response)
    response.raise_for_status()
except HTTPError as http_err:
    print(f"HTTP Error - {http_err}")
except Exception as err:
    print("Error")
else:
    with open("event_logs.txt", "wb") as events:
        for chunk in response.iter_content(chunk_size=10):
            print(chunk)
            events.write(chunk)

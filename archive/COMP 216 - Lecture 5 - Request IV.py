import requests
from requests.exceptions import HTTPError

url = 'https://api.github.com'

try:
    response = requests.get(url)
    response.raise_for_status()
except HTTPError as http_error:
    print(f'HTTP error occurred: {http_error}')
except Exception as e:
    print(f'Other error occurred: {e}')
else:
    header = response.headers  #Access header information as a dictionary- or map-like object
    print(header)
    
    date = header['Date']  #Access date value from the header
    content_type = header['Content-Type']  #Access the media type of the resource (e.g., plain text, CSS, JSON, etc.) from the header
    content_length = header['Content-Length']  #Access size of payload or body in bytes from the header
    
    print(f'{date}\r{content_type}\r{content_length}')
    
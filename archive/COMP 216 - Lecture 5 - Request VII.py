import requests
from requests.exceptions import HTTPError

# Example 1
url_jpg = 'https://httpbin.org/image/jpeg'

try:
    response = requests.get(url_jpg)  #GET request to download file
    response.raise_for_status()
except HTTPError as http_error:
    print(f'HTTP error occurred: {http_error}')
except Exception as e:
    print(f'Other error occurred: {e}')
else:
    with open('comp216pic.jpg', 'wb') as file:  #Opening/creating a file in binary mode to capture the response
        file.write(response.content)  #Write the response to file since the entire response is available in memory


# Example 2
url_svg = 'https://httpbin.org/image/svg'

try:
    response = requests.get(url_svg, stream=True)  #GET request to download file with stream parameter set to True
    response.raise_for_status()
except HTTPError as http_error:
    print(f'HTTP error occurred: {http_error}')
except Exception as e:
    print(f'Other error occurred: {e}')
else:
    with open('comp216svg.svg', 'wb') as file:
        for chunk in response.iter_content(chunk_size=128):  #When the stream parameter is set to True, iterates over the response data (e.g., only read 128 bytes into memory at a time)
            file.write(chunk)  #Write each chunk to the file as it becomes available in memory
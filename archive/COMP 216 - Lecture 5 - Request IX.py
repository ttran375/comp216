import requests
from requests.exceptions import Timeout  #Import class related to Timeout Errors from requests.exceptions module

# Example 1
url_png = 'https://httpbin.org/image/png'

response = requests.get(url_png, timeout=3)  #GET request to download file and specify timeout parameter (use integer or float value to indicate the number of seconds before timing out response)
with open('comp216pic.png', 'wb') as file:
    file.write(response.content)


# Example 2
response = requests.get(url_png, timeout=4.75)
with open('comp216pic_1.png', 'wb') as file:
    file.write(response.content)


# Example 3
response = requests.get(url_png, timeout=(3.5,6)) #specify timeout parameter as a tuple (timeout for establishing a connection between the client and server - initial handshake, timeout for receiving data after establishing connection)
with open('comp216pic_2.png', 'wb') as file:
    file.write(response.content)


# Example 4
try:
    response = requests.get(url_png, timeout=(3.5,6))
except Timeout:  #Exception raised when timeout value is reached
    print('Request has timed out')
else:
    with open('comp216pic_2.png', 'wb') as file:
        file.write(response.content)
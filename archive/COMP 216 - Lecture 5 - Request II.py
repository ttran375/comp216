import requests
from requests.exceptions import HTTPError  #Import class related to HTTP Errors from requests.exceptions module

for url in ['https://api.github.com', 'https://api1.github.com']:  #Iterate through multiple URLs
    try:
        response = requests.get(url)  #Perform GET command on each URL
        response.raise_for_status()  #Raise HTTP error for certain status codes; If response is successful, no Exceptions are raised
    except HTTPError as http_error:
        print(f'HTTP error occurred: {http_error}')  #Manage various HTTP errors
    except Exception as e:
        print(f'Other error occurred: {e}')  #Manage other types of Errors/issues
    else:
        print('Success')
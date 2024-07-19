import requests
from requests.adapters import HTTPAdapter  #Supports the creation of Transport Adapters to define configurations per service or endpoint
from requests.exceptions import ConnectionError  #Import class related to Connection errors (e.g., refusal to connect, no DNS response, etc.) from requests.exceptions module

url = 'https://api.github.com'
adapter = HTTPAdapter(max_retries=3)  #Create Transport Adapters to set max retries configuration for session connection

try:
    with requests.Session() as session:
        session.mount(url, adapter)  #For all requests related to the specified URL apply and maintain adapter configuration
        response = session.get('https://api.github.com')
except ConnectionError as conn_err:
    print(f'Connection Issue ... {conn_err}')  #Exception raised via a connection error
else:
    print(response.json())
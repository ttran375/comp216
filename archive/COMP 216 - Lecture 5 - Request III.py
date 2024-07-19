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
    cont = response.content  #Access payload or message body in bytes
    print(cont)
    print(type(cont))
    
    response.encoding = 'utf-8'  #Optional step to specify encoding for payload
    cont_text = response.text  #Access payload or message body in a string format
    print(cont_text)
    print(type(cont_text))
    
    cont_json = response.json()  #Access payload or message body in a dictionary (or JSON) format
    print(cont_json)
    print(type(cont_json))
    
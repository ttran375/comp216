import requests
from requests.exceptions import HTTPError
import base64  #Utilized to encode and decode binary to Base64

# Example 1
url = 'https://httpbin.org/post'  #Note each service or API will restrict commands based on the endpoint or URL

response = requests.post(url)  #Generate POST request without data
json_response = response.json()
print(json_response)
print('\n')


# Example 2
data = {'k1':'v1', 'k2':'v2', 'k3':'v3'}
response = requests.post(url, data=data)  #Generate POST request with data
json_response = response.json()
print(json_response)  #Note: Posted data is associated with the form field
print('\n')


# Example 3
new_data = {'k4':'v4', 'k5':'v5'}
response = requests.post(url, json=new_data)  #Generate separate and new POST request with different data point
json_response = response.json()
print(json_response)  #Note: Posted data is associated with the JSON and data fields, and past values are not present
print('\n')

posted_data = json_response['data']  #Access data fields and properties (a similar approach to retrieving information from a GET response)
date = response.headers['Date']
content_type = response.headers['Content-Type']
content_length = json_response['headers']['Content-Length']  #Also access header properties via nested dictionary query for this example
print(f'{posted_data}\r{date}\r{content_type}\r{content_length}')
print('\n')


# Example 4
filename = 'comp216pic.jpg'  #File retrieved from previous example
upload_file = open(filename, 'rb')  #Open and read JPG file in binary mode

try:
    response = requests.post(url, files={'files':upload_file})  #Generate POST request for file upload
    response.raise_for_status()
except HTTPError as http_error:
    print(f'HTTP error occurred: {http_error}')
except Exception as e:
    print(f'Other error occurred: {e}')
else:
    json_response = response.json()
    
    posted_file = json_response['files']  #Note: File value is not easily intrepreted by humans
    date = response.headers['Date']
    content_type = response.headers['Content-Type']  #Note: Content-type is set for JSON; however, uploading JPEG file
    content_length = json_response['headers']['Content-Length']
    print(f'{posted_file}\r{date}\r{content_type}\r{content_length}')
    print('\n')
finally:
    upload_file.close()  #Close JPG file


# Example 5
filename = 'comp216pic.jpg'
upload_file = open(filename, 'rb')

header_value = {'Content-Disposition':f'attachment; filename={filename}', 'Content-Type':'image/jpeg'}

try:
    response = requests.post(url, files={'files':upload_file}, headers=header_value)  #Generate POST request for file upload with updated headers
    response.raise_for_status()
except HTTPError as http_error:
    print(f'HTTP error occurred: {http_error}')
except Exception as e:
    print(f'Other error occurred: {e}')
else:
    json_response = response.json()
    posted_file = json_response['data']  #Note: File data is associated with the data field
    
    with open('check_upload.jpeg', 'wb') as file:  #Write a file from the response to extract uploaded file
        file.write(base64.b64decode(bytes(posted_file[posted_file.find('/9j'):], 'UTF-8')))  #Additional processing to decode and extract appropriate response image 
    
    name = json_response['headers']['Content-Disposition']
    content_type_1 = json_response['headers']['Content-Type']
    content_length_1 = json_response['headers']['Content-Length']
    print(f'{name}\r{content_type_1}\r{content_length_1}')
finally:
    upload_file.close()  #Close JPG file
import requests

# Example 1
response = requests.get('https://api.github.com/events', stream=True)  #When the stream parameter is set to True, the request will avoid downloading the response body (i.e., to prevent reading the whole body/file into memory) 

raw_object = response.raw  #When the stream parameter is set to True, it is possible to access the undecoded payload or message body
print(raw_object)
print(raw_object.read())  #Read raw output for the payload or body 


# Example 2
response = requests.get('https://api.github.com/events', stream=True)

with open('event_output.txt', 'wb') as f:  #Opening/creating a writeable file to capture the response
    for chunk in response.iter_content(chunk_size=10):  #When the stream parameter is set to True, iterates over the response data (e.g., only read 10 bytes into memory at a time); Avoids reading the content at once into memory for large responses
        print(chunk)
        f.write(chunk)  #Write chunk to file
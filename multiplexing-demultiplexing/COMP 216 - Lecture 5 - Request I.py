import requests  #Remember to install the library using the pip command from a terminal

# Example 1
response = requests.get('https://api.github.com')  #Perform common GET command to retrieve data from a specified resource
print(response)  #Displays status code of the request (e.g., 200 - successful request, 404 - resource not found, etc.)'


# Example 2
if response.status_code == 200:  #Conditional logic for successful status code
    print('Successful Request')
elif response.status_code == 404:  #Conditional logic for error status code
    print('Resource Not Found')
else:
    print('Other Status Code')


# Example 3
if response:  #Behaviour of request objects will establish a truth based on status code (e.g., 200 - 399 --> T; 400 - 599 --> F) 
    print('Successful Request')
else:
    print('Error with request')

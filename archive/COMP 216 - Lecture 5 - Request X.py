import requests

# Example 1
url_cookie = 'https://httpbin.org/cookies'

session = requests.Session()  #Establish a persistent connection and is utilized to persist parameters across requests

cookie_response = session.get('https://httpbin.org/cookies')  #Access cookie
print(cookie_response.text)

cookie_response = session.get('https://httpbin.org/cookies/set/sessioncookie/COMP216')  #Update cookie value
print(cookie_response.text)

cookie_response = session.get('https://httpbin.org/cookies/set/sessioncookie1/COMP217')  #Update cookie value
print(cookie_response.text)


# Example 2
with requests.Session() as session:  #Use context manager (with ... as ... construct) to ensure the session is released after executing instructions
    cookie_response = session.get('https://httpbin.org/cookies')  #Access cookie
    print(cookie_response.text)
    
    cookie_response = session.get('https://httpbin.org/cookies/set/sessioncookie/COMP216')  #Update cookie value
    print(cookie_response.text)
    
    cookie_response = session.get('https://httpbin.org/cookies/set/sessioncookie1/COMP217')  #Update cookie value
    print(cookie_response.headers)
    print(cookie_response.text)
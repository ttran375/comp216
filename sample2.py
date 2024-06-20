import requests

url = "https://httpbin.org/cookies"
ns_response = requests.get(url)
print(ns_response.text)

ns_response_1 = requests.get(url + "/set/input1/value1")
print(ns_response_1.text)

ns_response_2 = requests.get(url + "/set/input2/value2")
print(ns_response_2.text)

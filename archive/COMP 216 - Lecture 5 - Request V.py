import requests
from requests.exceptions import HTTPError

# Example 1
try:
    response = requests.get('https://api.github.com/search/repositories',  #URL for GitHub Search API (See https://docs.github.com/en/rest/search?apiVersion=2022-11-28#search-repositories)
                            params = {'q': 'requests+language:python'},  #Specify search parameters as dictionary {'query keyword' : 'search term'}
                            headers={'Accept':'application/vnd.github.v3/text-match+json'}  #Specify Accept header paramaters in order to highlight matching search terms when displaying the results 
                            )
    response.raise_for_status()
except HTTPError as http_error:
    print(f'HTTP error occurred: {http_error}')
except Exception as e:
    print(f'Other error occurred: {e}')
else:
    print(response.url)  #URL of Request (e.g., https://api.github.com/search/repositories?q=requests%2Blanguage%3Apython)
    print('\n')
    
    response_json = response.json()
    first_result = response_json['items'][0]  #Retrieve all information regarding the first search result
    print(first_result)
    print('\n')
    
    second_result = response_json['items'][1]  #Retrieve all information regarding the second search result 
    print(f'Repo ID: {second_result["id"]}, Repo Name: {second_result["name"]} \nRepo URL: {second_result["url"]}') #Retrieve selected pieces of information for second search result
    print('\n')


# Example 2
try:
    response = requests.get('https://api.github.com/search/repositories',
                            params = [('q','requests+language:python')],  #Specify search parameters as List of tuple(s) [('query keyword','search term')]
                            headers={'Accept':'application/vnd.github.v3/text-match+json'}
                            )
    response.raise_for_status()
except HTTPError as http_error:
    print(f'HTTP error occurred: {http_error}')
except Exception as e:
    print(f'Other error occurred: {e}')
else:
    print(response.url)
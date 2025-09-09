import requests
from requests.exceptions import HTTPError
response = requests.get('https://api.github.com')
response.encoding="utf-8"
#print(response.text)
response_dict = response.json()
print(response_dict['current_user_url'])
print(response.headers)


'''URLS = ['https://api.github.com', 'https://api.github.com/invalid']
for url in URLS:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!')'''
'''response = requests.get('https://api.github.com')
if response.status_code == 200:
    print('Success!')
else:
    print('An error has occurred.')'''
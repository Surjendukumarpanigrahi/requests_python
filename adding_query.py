import requests
response = requests.get('https://api.github.com/search/repositories',
                        params={'q': ' "real python" '},
                        headers = {'Accept' : 'application/vnd.github.text-match+json'})
json_response = response.json()
#print(json_response)
first_repo = json_response['items'][0]
print(first_repo['text_matches'][0]['matches'])

'''popular_repos =json_response['items']
for repo in popular_repos[:5]:
    print(f"Name: {repo['name']}")
    print(f"Description: {repo['description']}")
    print(f"Stars: {repo['stargazers_count']}\n")'''
          
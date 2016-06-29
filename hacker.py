import requests 

from operator import itemgetter

#Make an API Call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Status Code:', r.status_code)

#Process information about each submission
submission_ids = r.json() 
#Storing all of the dictionaries in an empty list.
submission_dicts = []

print(submission_dicts)
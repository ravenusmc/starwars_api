import requests 

#Setting up the URL that I will be looking at.
url = ('http://swapi.co/api/starships')
#Setting up a get request to pull the data from the URL
r = requests.get(url)
# if r.status_code == 200:
#   print("status_code", r.status_code)
#   print("You have connected to the database!")
# else:
#   print("Sorry it appears your connection failed!")

response_dict = r.json()

repo_dicts = response_dict['results']

num = 0
while num < response_dict['count']:
  if num >= 0 and num <= 9:
    url = ('http://swapi.co/api/starships')
    r = requests.get(url)
    response_dict = r.json()
    repo_dict = repo_dicts[num]['name']
    print(str(num) + " " + repo_dict)
  elif num > 10 and num <= 19:
    url = ('http://swapi.co/api/starships/?format=json&page=2')
    r = requests.get(url)
    print("status_code, page 2", r.status_code)
    response_dict = r.json()
    #repo_dict = repo_dicts[num]['name']
    # print("test3")
    # print(str(num) + " " + repo_dict)
  elif num > 19 and num <= 29:
    url = ('http://swapi.co/api/starships/?format=json&page=3')
    r = requests.get(url)
    print("status_code, page 3", r.status_code)
    response_dict = r.json()
  #   repo_dict = repo_dicts[num]['name']
  #   print(str(num) + " " + repo_dict)
  elif num > 29 and num <= 36:
    url = ('http://swapi.co/api/starships/?format=json&page=4')
    r = requests.get(url)
    print("status_code, page 4", r.status_code)
    response_dict = r.json()
  #   repo_dict = repo_dicts[num]['name']
  #   print(str(num) + " " + repo_dict)
  
  num += 1 
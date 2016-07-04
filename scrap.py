#This program will use the http://swapi.co/api/ api which will allow the user to look at
#star wars data. 

import requests 

def connect(view):
  #Setting up the URL that I will be looking at.
  url = ('http://swapi.co/api/' + str(view))
  #Setting up a get request to pull the data from the URL
  r = requests.get(url)
  if r.status_code == 200:
    print("status_code", r.status_code)
    print("You have connected to the database!")
  else:
    print("Sorry it appears your connection failed!")

  #Storing the API response in a variable 
  response_dict = r.json()
  print("There are currently", response_dict['count'], "items to view")

  print("Here are the " + view + " that you can see:")

  repo_dicts = response_dict['results']

  num = 0
  while num < response_dict['count']:
    if view == 'films':
      repo_dict = repo_dicts[num]['title']
      print(str(num) + " " + repo_dict)
    elif view == 'starships':
      repo_dict = repo_dicts[num]['name']
      print(str(num) + " " + repo_dict)
    num += 1 

  choice = int(input("Which one do you want to look at: "))
  print("Here is the information on the " + view + " you wanted to see: ")
  # print(repo_dicts[choice])
  items = []
  item = {
    "title": response_dict['results'][choice]['title'],
    "episode_id": response_dict['results'][choice]['episode_id'],
    "opening_crawl": response_dict['results'][choice]['opening_crawl'],
    "director": response_dict['results'][choice]['director'],
    "producer": response_dict['results'][choice]['producer'],
    "release_date": response_dict['results'][choice]['release_date'],
    "characters": response_dict['results'][choice]['characters'],
  }

  items.append(item)

  for item in items:
    print("Title:", item['title'])
    print("episode:", response_dict['results'][choice]['episode_id'])
    print("Director:", item['director'])
    print("Producer:", item['producer'])
    print("release_date", item['release_date'])
    print("opening_crawl:", item['opening_crawl'])


########## This Code is GOOD!!!
  # num = 0
  # while num < response_dict['count']:
  #   if view == 'films':
  #     repo_dict = repo_dicts[num]['title']
  #     print(str(num) + " " + repo_dict)
  #   elif view == 'starships': 
  #     repo_dict = repo_dicts[num]['name']
  #     print(str(num) + " " + repo_dict)
  #   num += 1 

  # choice = int(input("Which one do you want to look at: "))
  # print("Here is the information on the " + view + "You wanted to see: ")
  # print(repo_dicts[choice])
###################

def began():
  print("To start, Here are the categories you can look at:")
  print("people")
  print("planets")
  print("films")
  print("species")
  print("vehicles")
  print("starships")
  view = input("What do you want to look at? ")
  connect(view)


#This function starts the program and basically asks the user if
#they want to use it. 
def main():
  print('*******************')
  print('---STAR WARS API--- ')
  print('*******************')
  choice = input("Would you like to use it?(y/n) ")
  if choice.lower() == "y":
    began()
  else:
    print("Hope you use it soon!")

main()

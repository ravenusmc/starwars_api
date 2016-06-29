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
  print("Total count: ", response_dict['count'])
  #Here I am looking at the Key Results-this key happens to have all the information that 
  #I need to look at the information. 
  repo_dicts = response_dict['results']


  for key, value in repo_dicts:
    print(repo_dicts['title'])

  repo_dict = repo_dicts[1]
  print("Here is what you can look at:")
  for key in sorted(repo_dict.keys()):
    print(key)
  print("From the above list, what do you want to examine?")














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


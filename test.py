import requests 

############## START OF FILMS ##################

def films():
  #Setting up the URL that I will be looking at.
  url = ('http://swapi.co/api/films')
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

  print("Here are the films that you can see:")

  repo_dicts = response_dict['results']

  num = 0
  while num < response_dict['count']:
    repo_dict = repo_dicts[num]['title']
    print(str(num) + " " + repo_dict)
    num += 1 

  choice = int(input("Which one do you want to look at: "))
  print("Here is the information you wanted to see: ")
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

############# END OF FILMS #####################


################ START OF STARSHIPS #############

def starship():
  print("Here you will find information about Starships in Star Wars")
  print("There are a lot of ships which will be in groups of 10.")
  print("Please choose which group you want to look at:")
  print("1: First Group")
  print("2: Second Group")
  print("3: Third Group")
  print("4: Fourth Group")
  choice = int(input("What do you want to look at: "))
  if choice == 1:
    two()


def two():
  num = 0
  while num <= 9:
    if num >= 0 and num <= 10:
      url = ('http://swapi.co/api/starships/?page=2')
      r = requests.get(url)
      response_dict = r.json()
      repo_dicts = response_dict['results']
      repo_dict = repo_dicts[num]['name']
      print(str(num) + " " + repo_dict)
      num += 1 

  print("If you do not see your ship please enter -1 to go back to the main starship menu")
  choice = int(input("Which one do you want to look at: "))
  if choice == -1:
    starship()
  print("Here is the information on the you wanted to see: ")

  items = []
  item = {
    "name": response_dict['results'][choice]['name'],
    "model": response_dict['results'][choice]['model'],
    "manufacturer": response_dict['results'][choice]['manufacturer'],
    "length": response_dict['results'][choice]['length'],
    "max_atmosphering_speed": response_dict['results'][choice]['max_atmosphering_speed'],
    "crew": response_dict['results'][choice]['crew'],
    "cargo_capacity": response_dict['results'][choice]['cargo_capacity'],
    "consumables": response_dict['results'][choice]['consumables'],
    "hyperdrive_rating": response_dict['results'][choice]['hyperdrive_rating'],
    "starship_class": response_dict['results'][choice]['starship_class']
  }

  items.append(item)

  for item in items:
    print("name:", item['name'])
    print("model:", item['model'])
    print("Manufacturer:", item['manufacturer'])
    print("Length:", item['length'])
    print("max_atmosphering_speed:", item['max_atmosphering_speed'])
    print("crew:", item['crew'])
    print("cargo_capacity:", item['cargo_capacity'])
    print("consumables:", item['consumables'])
    print("hyperdrive_rating:", item['hyperdrive_rating'])
    print("starship_class:", item['starship_class'])


def three():
  num = 0
  while num <= 9:
    if num >= 0 and num <= 9:
      url = ('http://swapi.co/api/starships/?page=3')
      r = requests.get(url)
      response_dict = r.json()
      repo_dicts = response_dict['results']
      repo_dict = repo_dicts[num]['name']
      print(str(num) + " " + repo_dict)
      num += 1 

  print("If you do not see your ship please enter -1 to go back to the main starship menu")
  choice = int(input("Which one do you want to look at: "))
  if choice == -1:
    starship()
  print("Here is the information on the you wanted to see: ")

  items = []
  item = {
    "name": response_dict['results'][choice]['name'],
    "model": response_dict['results'][choice]['model'],
    "manufacturer": response_dict['results'][choice]['manufacturer'],
    "length": response_dict['results'][choice]['length'],
    "max_atmosphering_speed": response_dict['results'][choice]['max_atmosphering_speed'],
    "crew": response_dict['results'][choice]['crew'],
    "cargo_capacity": response_dict['results'][choice]['cargo_capacity'],
    "consumables": response_dict['results'][choice]['consumables'],
    "hyperdrive_rating": response_dict['results'][choice]['hyperdrive_rating'],
    "starship_class": response_dict['results'][choice]['starship_class']
  }

  items.append(item)

  for item in items:
    print("name:", item['name'])
    print("model:", item['model'])
    print("Manufacturer:", item['manufacturer'])
    print("Length:", item['length'])
    print("max_atmosphering_speed:", item['max_atmosphering_speed'])
    print("crew:", item['crew'])
    print("cargo_capacity:", item['cargo_capacity'])
    print("consumables:", item['consumables'])
    print("hyperdrive_rating:", item['hyperdrive_rating'])
    print("starship_class:", item['starship_class'])

def four():
  num = 0
  while num <= 6:
    if num >= 0 and num <= 9:
      url = ('http://swapi.co/api/starships/?page=4')
      r = requests.get(url)
      response_dict = r.json()
      repo_dicts = response_dict['results']
      repo_dict = repo_dicts[num]['name']
      print(str(num) + " " + repo_dict)
      num += 1 

  print("If you do not see your ship please enter -1 to go back to the main starship menu")
  choice = int(input("Which one do you want to look at: "))
  if choice == -1:
    starship()
  print("Here is the information on the you wanted to see: ")

  items = []
  item = {
    "name": response_dict['results'][choice]['name'],
    "model": response_dict['results'][choice]['model'],
    "manufacturer": response_dict['results'][choice]['manufacturer'],
    "length": response_dict['results'][choice]['length'],
    "max_atmosphering_speed": response_dict['results'][choice]['max_atmosphering_speed'],
    "crew": response_dict['results'][choice]['crew'],
    "cargo_capacity": response_dict['results'][choice]['cargo_capacity'],
    "consumables": response_dict['results'][choice]['consumables'],
    "hyperdrive_rating": response_dict['results'][choice]['hyperdrive_rating'],
    "starship_class": response_dict['results'][choice]['starship_class']
  }

  items.append(item)

  for item in items:
    print("name:", item['name'])
    print("model:", item['model'])
    print("Manufacturer:", item['manufacturer'])
    print("Length:", item['length'])
    print("max_atmosphering_speed:", item['max_atmosphering_speed'])
    print("crew:", item['crew'])
    print("cargo_capacity:", item['cargo_capacity'])
    print("consumables:", item['consumables'])
    print("hyperdrive_rating:", item['hyperdrive_rating'])
    print("starship_class:", item['starship_class'])

################# END OF STARSHIPS #################

def began():
  print("To start, Here are the categories you can look at:")
  print("1. People")
  print("2. Planets")
  print("3. Films")
  print("4. Species")
  print("5. Vehicles")
  print("6. Starships")
  choice = int(input("What do you want to look at? "))
  if choice == 1:
    films()
  elif choice == 3:
    films()
  elif choice == 6:
    starship()
  


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

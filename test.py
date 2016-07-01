import requests 

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

  choice = int(input("Which one do you want to look at: "))
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

  choice = int(input("Which one do you want to look at: "))
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

  choice = int(input("Which one do you want to look at: "))
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


def began():
  print("To start, Here are the categories you can look at:")
  print("people")
  print("planets")
  print("films")
  print("species")
  print("vehicles")
  print("starships")
  view = input("What do you want to look at? ")
  
  

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

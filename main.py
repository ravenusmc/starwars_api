import requests 

############## START OF PEOPLE ##################

def people():
  print("Here you will find information about People in Star Wars")
  print("There are a lot of people which will be in groups of 10.")
  print("Please choose which group you want to look at:")
  print("1: First Group")
  print("2: Second Group")
  print("3: Third Group")
  print("4: Fourth Group")
  print("5: Fifth Group")
  print("6: Sixth Group")
  print("7: Seventh Group")
  print("8: Eigth Group")
  print("9: Ninth Group")
  choice = int(input("What do you want to look at: "))
  if choice == 1:
    firstP()
  elif choice == 2:
    secondP()
  elif choice == 3:
    thirdP()
  elif choice == 4:
    fourthP()
  elif choice == 5:
    fifthP()
  elif choice == 6:
    sixthP()
  elif choice == 7:
    seventhP()
  elif choice == 8:
    eighthP()
  elif choice == 9:
    ninthP()

def firstP():
  num = 0
  while num <= 9:
    if num >= 0 and num <= 10:
      url = ('http://swapi.co/api/people/')
      r = requests.get(url)
      response_dict = r.json()
      repo_dicts = response_dict['results']
      repo_dict = repo_dicts[num]['name']
      print(str(num) + " " + repo_dict)
      num += 1 

  print("If you do not see your person please enter -1 to go back to the main starship menu")
  choice = int(input("Which one do you want to look at: "))
  if choice == -1:
    people()
  print("Here is the information on the you wanted to see: ")

  items = []
  item = {
    "name": response_dict['results'][choice]['name'],
    "height": response_dict['results'][choice]['height'],
    "mass": response_dict['results'][choice]['mass'],
    "hair_color": response_dict['results'][choice]['hair_color'],
    "skin_color": response_dict['results'][choice]['skin_color'],
    "eye_color": response_dict['results'][choice]['eye_color'],
    "birth_year": response_dict['results'][choice]['birth_year'],
    "gender": response_dict['results'][choice]['gender'],
    "homeworld": response_dict['results'][choice]['homeworld'],
  }

  items.append(item)

  for item in items:
    print("name:", item['name'])
    print("height:", item['height'])
    print("Mass:", item['mass'])
    print("hair_color:", item['hair_color'])
    print("skin_color", item['skin_color'])
    print("eye_color", item['eye_color'])
    print("birth_year", item['birth_year'])
    print("gender:", item['gender'])
    print("homeworld", item['homeworld'])
  
  option = input("Do you want to continue using program or exit? (y/n) ")
  while not validP(option):
    print("That is not a valid selection")
    option = input("Do you want to continue using program or exit? (y/n) ")
  if option == "y":
    began()
  elif option == "n":
    print("Thank you for using the program!")

def secondP():
  num = 0
  while num <= 9:
    if num >= 0 and num <= 10:
      url = ('http://swapi.co/api/people/?page=2')
      r = requests.get(url)
      response_dict = r.json()
      repo_dicts = response_dict['results']
      repo_dict = repo_dicts[num]['name']
      print(str(num) + " " + repo_dict)
      num += 1 

  print("If you do not see your person please enter -1 to go back to the main starship menu")
  choice = int(input("Which one do you want to look at: "))
  if choice == -1:
    people()
  print("Here is the information on the you wanted to see: ")

  items = []
  item = {
    "name": response_dict['results'][choice]['name'],
    "height": response_dict['results'][choice]['height'],
    "mass": response_dict['results'][choice]['mass'],
    "hair_color": response_dict['results'][choice]['hair_color'],
    "skin_color": response_dict['results'][choice]['skin_color'],
    "eye_color": response_dict['results'][choice]['eye_color'],
    "birth_year": response_dict['results'][choice]['birth_year'],
    "gender": response_dict['results'][choice]['gender']
  }

  items.append(item)

  for item in items:
    print("name:", item['name'])
    print("height:", item['height'])
    print("Mass:", item['mass'])
    print("hair_color:", item['hair_color'])
    print("skin_color", item['skin_color'])
    print("eye_color", item['eye_color'])
    print("birth_year", item['birth_year'])
    print("gender:", item['gender'])
  
  option = input("Do you want to continue using program or exit? (y/n) ")
  while not validP(option):
    print("That is not a valid selection")
    option = input("Do you want to continue using program or exit? (y/n) ")
  if option == "y":
    began()
  elif option == "n":
    print("Thank you for using the program!")

def thirdP():
  num = 0
  while num <= 9:
    if num >= 0 and num <= 10:
      url = ('http://swapi.co/api/people/?page=3')
      r = requests.get(url)
      response_dict = r.json()
      repo_dicts = response_dict['results']
      repo_dict = repo_dicts[num]['name']
      print(str(num) + " " + repo_dict)
      num += 1 

  print("If you do not see your person please enter -1 to go back to the main starship menu")
  choice = int(input("Which one do you want to look at: "))
  if choice == -1:
    people()
  print("Here is the information on the you wanted to see: ")

  items = []
  item = {
    "name": response_dict['results'][choice]['name'],
    "height": response_dict['results'][choice]['height'],
    "mass": response_dict['results'][choice]['mass'],
    "hair_color": response_dict['results'][choice]['hair_color'],
    "skin_color": response_dict['results'][choice]['skin_color'],
    "eye_color": response_dict['results'][choice]['eye_color'],
    "birth_year": response_dict['results'][choice]['birth_year'],
    "gender": response_dict['results'][choice]['gender'],
    "homeworld": response_dict['results'][choice]['homeworld'],
  }

  items.append(item)

  for item in items:
    print("name:", item['name'])
    print("height:", item['height'])
    print("Mass:", item['mass'])
    print("hair_color:", item['hair_color'])
    print("skin_color", item['skin_color'])
    print("eye_color", item['eye_color'])
    print("birth_year", item['birth_year'])
    print("gender:", item['gender'])
    print("homeworld", item['homeworld'])

  option = input("Do you want to continue using program or exit? (y/n) ")
  while not validP(option):
    print("That is not a valid selection")
    option = input("Do you want to continue using program or exit? (y/n) ")
  if option == "y":
    began()
  elif option == "n":
    print("Thank you for using the program!")

def fourthP():
  num = 0
  while num <= 9:
    if num >= 0 and num <= 10:
      url = ('http://swapi.co/api/people/?page=4')
      r = requests.get(url)
      response_dict = r.json()
      repo_dicts = response_dict['results']
      repo_dict = repo_dicts[num]['name']
      print(str(num) + " " + repo_dict)
      num += 1 

  print("If you do not see your person please enter -1 to go back to the main starship menu")
  choice = int(input("Which one do you want to look at: "))
  if choice == -1:
    people()
  print("Here is the information on the you wanted to see: ")

  items = []
  item = {
    "name": response_dict['results'][choice]['name'],
    "height": response_dict['results'][choice]['height'],
    "mass": response_dict['results'][choice]['mass'],
    "hair_color": response_dict['results'][choice]['hair_color'],
    "skin_color": response_dict['results'][choice]['skin_color'],
    "eye_color": response_dict['results'][choice]['eye_color'],
    "birth_year": response_dict['results'][choice]['birth_year'],
    "gender": response_dict['results'][choice]['gender']
  }

  items.append(item)

  for item in items:
    print("name:", item['name'])
    print("height:", item['height'])
    print("Mass:", item['mass'])
    print("hair_color:", item['hair_color'])
    print("skin_color", item['skin_color'])
    print("eye_color", item['eye_color'])
    print("birth_year", item['birth_year'])
    print("gender:", item['gender'])

  option = input("Do you want to continue using program or exit? (y/n) ")
  while not validP(option):
    print("That is not a valid selection")
    option = input("Do you want to continue using program or exit? (y/n) ")
  if option == "y":
    began()
  elif option == "n":
    print("Thank you for using the program!")

def fifthP():
  num = 0
  while num <= 9:
    if num >= 0 and num <= 10:
      url = ('http://swapi.co/api/people/?page=5')
      r = requests.get(url)
      response_dict = r.json()
      repo_dicts = response_dict['results']
      repo_dict = repo_dicts[num]['name']
      print(str(num) + " " + repo_dict)
      num += 1 

  print("If you do not see your person please enter -1 to go back to the main starship menu")
  choice = int(input("Which one do you want to look at: "))
  if choice == -1:
    people()
  print("Here is the information on the you wanted to see: ")

  items = []
  item = {
    "name": response_dict['results'][choice]['name'],
    "height": response_dict['results'][choice]['height'],
    "mass": response_dict['results'][choice]['mass'],
    "hair_color": response_dict['results'][choice]['hair_color'],
    "skin_color": response_dict['results'][choice]['skin_color'],
    "eye_color": response_dict['results'][choice]['eye_color'],
    "birth_year": response_dict['results'][choice]['birth_year'],
    "gender": response_dict['results'][choice]['gender']
  }

  items.append(item)

  for item in items:
    print("name:", item['name'])
    print("height:", item['height'])
    print("Mass:", item['mass'])
    print("hair_color:", item['hair_color'])
    print("skin_color", item['skin_color'])
    print("eye_color", item['eye_color'])
    print("birth_year", item['birth_year'])
    print("gender:", item['gender'])

  option = input("Do you want to continue using program or exit? (y/n) ")
  while not validP(option):
    print("That is not a valid selection")
    option = input("Do you want to continue using program or exit? (y/n) ")
  if option == "y":
    began()
  elif option == "n":
    print("Thank you for using the program!")

def sixthP():
  num = 0
  while num <= 9:
    if num >= 0 and num <= 10:
      url = ('http://swapi.co/api/people/?page=6')
      r = requests.get(url)
      response_dict = r.json()
      repo_dicts = response_dict['results']
      repo_dict = repo_dicts[num]['name']
      print(str(num) + " " + repo_dict)
      num += 1 

  print("If you do not see your person please enter -1 to go back to the main starship menu")
  choice = int(input("Which one do you want to look at: "))
  if choice == -1:
    people()
  print("Here is the information on the you wanted to see: ")

  items = []
  item = {
    "name": response_dict['results'][choice]['name'],
    "height": response_dict['results'][choice]['height'],
    "mass": response_dict['results'][choice]['mass'],
    "hair_color": response_dict['results'][choice]['hair_color'],
    "skin_color": response_dict['results'][choice]['skin_color'],
    "eye_color": response_dict['results'][choice]['eye_color'],
    "birth_year": response_dict['results'][choice]['birth_year'],
    "gender": response_dict['results'][choice]['gender']
  }

  items.append(item)

  for item in items:
    print("name:", item['name'])
    print("height:", item['height'])
    print("Mass:", item['mass'])
    print("hair_color:", item['hair_color'])
    print("skin_color", item['skin_color'])
    print("eye_color", item['eye_color'])
    print("birth_year", item['birth_year'])
    print("gender:", item['gender'])

  option = input("Do you want to continue using program or exit? (y/n) ")
  while not validP(option):
    print("That is not a valid selection")
    option = input("Do you want to continue using program or exit? (y/n) ")
  if option == "y":
    began()
  elif option == "n":
    print("Thank you for using the program!")


def seventhP():
  num = 0
  while num <= 9:
    if num >= 0 and num <= 10:
      url = ('http://swapi.co/api/people/?page=7')
      r = requests.get(url)
      response_dict = r.json()
      repo_dicts = response_dict['results']
      repo_dict = repo_dicts[num]['name']
      print(str(num) + " " + repo_dict)
      num += 1 

  print("If you do not see your person please enter -1 to go back to the main starship menu")
  choice = int(input("Which one do you want to look at: "))
  if choice == -1:
    people()
  print("Here is the information on the you wanted to see: ")

  items = []
  item = {
    "name": response_dict['results'][choice]['name'],
    "height": response_dict['results'][choice]['height'],
    "mass": response_dict['results'][choice]['mass'],
    "hair_color": response_dict['results'][choice]['hair_color'],
    "skin_color": response_dict['results'][choice]['skin_color'],
    "eye_color": response_dict['results'][choice]['eye_color'],
    "birth_year": response_dict['results'][choice]['birth_year'],
    "gender": response_dict['results'][choice]['gender']
  }

  items.append(item)

  for item in items:
    print("name:", item['name'])
    print("height:", item['height'])
    print("Mass:", item['mass'])
    print("hair_color:", item['hair_color'])
    print("skin_color", item['skin_color'])
    print("eye_color", item['eye_color'])
    print("birth_year", item['birth_year'])
    print("gender:", item['gender'])

  option = input("Do you want to continue using program or exit? (y/n) ")
  while not validP(option):
    print("That is not a valid selection")
    option = input("Do you want to continue using program or exit? (y/n) ")
  if option == "y":
    began()
  elif option == "n":
    print("Thank you for using the program!")


def eighthP():
  num = 0
  while num <= 9:
    if num >= 0 and num <= 10:
      url = ('http://swapi.co/api/people/?page=8')
      r = requests.get(url)
      response_dict = r.json()
      repo_dicts = response_dict['results']
      repo_dict = repo_dicts[num]['name']
      print(str(num) + " " + repo_dict)
      num += 1 

  print("If you do not see your person please enter -1 to go back to the main starship menu")
  choice = int(input("Which one do you want to look at: "))
  if choice == -1:
    people()
  print("Here is the information on the you wanted to see: ")

  items = []
  item = {
    "name": response_dict['results'][choice]['name'],
    "height": response_dict['results'][choice]['height'],
    "mass": response_dict['results'][choice]['mass'],
    "hair_color": response_dict['results'][choice]['hair_color'],
    "skin_color": response_dict['results'][choice]['skin_color'],
    "eye_color": response_dict['results'][choice]['eye_color'],
    "birth_year": response_dict['results'][choice]['birth_year'],
    "gender": response_dict['results'][choice]['gender']
  }

  items.append(item)

  for item in items:
    print("name:", item['name'])
    print("height:", item['height'])
    print("Mass:", item['mass'])
    print("hair_color:", item['hair_color'])
    print("skin_color", item['skin_color'])
    print("eye_color", item['eye_color'])
    print("birth_year", item['birth_year'])
    print("gender:", item['gender'])

  option = input("Do you want to continue using program or exit? (y/n) ")
  while not validP(option):
    print("That is not a valid selection")
    option = input("Do you want to continue using program or exit? (y/n) ")
  if option == "y":
    began()
  elif option == "n":
    print("Thank you for using the program!")

def ninthP():
  num = 0
  while num <= 6:
    if num >= 0 and num <= 6:
      url = ('http://swapi.co/api/people/?page=9')
      r = requests.get(url)
      response_dict = r.json()
      repo_dicts = response_dict['results']
      repo_dict = repo_dicts[num]['name']
      print(str(num) + " " + repo_dict)
      num += 1 

  print("If you do not see your person please enter -1 to go back to the main starship menu")
  choice = int(input("Which one do you want to look at: "))
  if choice == -1:
    people()
  print("Here is the information on the you wanted to see: ")

  items = []
  item = {
    "name": response_dict['results'][choice]['name'],
    "height": response_dict['results'][choice]['height'],
    "mass": response_dict['results'][choice]['mass'],
    "hair_color": response_dict['results'][choice]['hair_color'],
    "skin_color": response_dict['results'][choice]['skin_color'],
    "eye_color": response_dict['results'][choice]['eye_color'],
    "birth_year": response_dict['results'][choice]['birth_year'],
    "gender": response_dict['results'][choice]['gender']
  }

  items.append(item)

  for item in items:
    print("name:", item['name'])
    print("height:", item['height'])
    print("Mass:", item['mass'])
    print("hair_color:", item['hair_color'])
    print("skin_color", item['skin_color'])
    print("eye_color", item['eye_color'])
    print("birth_year", item['birth_year'])
    print("gender:", item['gender'])

  option = input("Do you want to continue using program or exit? (y/n) ")
  while not validP(option):
    print("That is not a valid selection")
    option = input("Do you want to continue using program or exit? (y/n) ")
  if option == "y":
    began()
  elif option == "n":
    print("Thank you for using the program!")



############# END OF PEOPLE #####################

############## START OF PLANETS ##################

def planets():
  print("Here you will find information about Planets in Star Wars")
  print("There are a lot of people which will be in groups of 6.")
  print("Please choose which group you want to look at:")
  print("1: First Group")
  print("2: Second Group")
  print("3: Third Group")
  print("4: Fourth Group")
  print("5: Fifth Group")
  print("6: Sixth Group")
  print("7: Seventh Group")
  choice = int(input("What do you want to look at: "))
  if choice == 1:
    onePl()
  elif choice == 2:
    twoPl()
  elif choice == 3:
    threePl()
  elif choice == 4:
    fourPl()
  elif choice == 5:
    fivePl()
  elif choice == 6:
    sixPl()
  elif choice == 7:
    sevenPl()

def onePl():
  num = 0
  while num <= 9:
    if num >= 0 and num <= 10:
      url = ('http://swapi.co/api/planets/')
      r = requests.get(url)
      response_dict = r.json()
      repo_dicts = response_dict['results']
      repo_dict = repo_dicts[num]['name']
      print(str(num) + " " + repo_dict)
      num += 1 

  print("If you do not see your planet please enter -1 to go back to the main starship menu")
  choice = int(input("Which one do you want to look at: "))
  if choice == -1:
    starship()
  print("Here is the information on the you wanted to see: ")

  items = []
  item = {
    "name": response_dict['results'][choice]['name'],
    "rotation_period": response_dict['results'][choice]['rotation_period'],
    "orbital_period": response_dict['results'][choice]['orbital_period'],
    "diameter": response_dict['results'][choice]['diameter'],
    "climate": response_dict['results'][choice]['climate'],
    "gravity": response_dict['results'][choice]['gravity'],
    "terrain": response_dict['results'][choice]['terrain'],
    "surface_water": response_dict['results'][choice]['surface_water'],
    "population": response_dict['results'][choice]['population']
  }

  items.append(item)

  for item in items:
    print("name:", item['name'])
    print("rotation_period:", item['rotation_period'])
    print("orbital_period:", item['orbital_period'])
    print("diameter", item['diameter'])
    print("climate", item['climate'])
    print("gravity", item['gravity'])
    print("terrain", item['terrain'])
    print("surface_water", item['surface_water'])
    print("population", item['population'])

  option = input("Do you want to continue using program or exit? (y/n) ")
  while not validP(option):
    print("That is not a valid selection")
    option = input("Do you want to continue using program or exit? (y/n) ")
  if option == "y":
    began()
  elif option == "n":
    print("Thank you for using the program!")

def twoPl():
  num = 0
  while num <= 9:
    if num >= 0 and num <= 10:
      url = ('http://swapi.co/api/planets/?page=2')
      r = requests.get(url)
      response_dict = r.json()
      repo_dicts = response_dict['results']
      repo_dict = repo_dicts[num]['name']
      print(str(num) + " " + repo_dict)
      num += 1 

  print("If you do not see your planet please enter -1 to go back to the main starship menu")
  choice = int(input("Which one do you want to look at: "))
  if choice == -1:
    starship()
  print("Here is the information on the you wanted to see: ")

  items = []
  item = {
    "name": response_dict['results'][choice]['name'],
    "rotation_period": response_dict['results'][choice]['rotation_period'],
    "orbital_period": response_dict['results'][choice]['orbital_period'],
    "diameter": response_dict['results'][choice]['diameter'],
    "climate": response_dict['results'][choice]['climate'],
    "gravity": response_dict['results'][choice]['gravity'],
    "terrain": response_dict['results'][choice]['terrain'],
    "surface_water": response_dict['results'][choice]['surface_water'],
    "population": response_dict['results'][choice]['population']
  }

  items.append(item)

  for item in items:
    print("name:", item['name'])
    print("rotation_period:", item['rotation_period'])
    print("orbital_period:", item['orbital_period'])
    print("diameter", item['diameter'])
    print("climate", item['climate'])
    print("gravity", item['gravity'])
    print("terrain", item['terrain'])
    print("surface_water", item['surface_water'])
    print("population", item['population'])

  option = input("Do you want to continue using program or exit? (y/n) ")
  while not validP(option):
    print("That is not a valid selection")
    option = input("Do you want to continue using program or exit? (y/n) ")
  if option == "y":
    began()
  elif option == "n":
    print("Thank you for using the program!")

def thirdPl():
  num = 0
  while num <= 9:
    if num >= 0 and num <= 10:
      url = ('http://swapi.co/api/planets/?page=3')
      r = requests.get(url)
      response_dict = r.json()
      repo_dicts = response_dict['results']
      repo_dict = repo_dicts[num]['name']
      print(str(num) + " " + repo_dict)
      num += 1 

  print("If you do not see your planet please enter -1 to go back to the main starship menu")
  choice = int(input("Which one do you want to look at: "))
  if choice == -1:
    starship()
  print("Here is the information on the you wanted to see: ")

  items = []
  item = {
    "name": response_dict['results'][choice]['name'],
    "rotation_period": response_dict['results'][choice]['rotation_period'],
    "orbital_period": response_dict['results'][choice]['orbital_period'],
    "diameter": response_dict['results'][choice]['diameter'],
    "climate": response_dict['results'][choice]['climate'],
    "gravity": response_dict['results'][choice]['gravity'],
    "terrain": response_dict['results'][choice]['terrain'],
    "surface_water": response_dict['results'][choice]['surface_water'],
    "population": response_dict['results'][choice]['population']
  }

  items.append(item)

  for item in items:
    print("name:", item['name'])
    print("rotation_period:", item['rotation_period'])
    print("orbital_period:", item['orbital_period'])
    print("diameter", item['diameter'])
    print("climate", item['climate'])
    print("gravity", item['gravity'])
    print("terrain", item['terrain'])
    print("surface_water", item['surface_water'])
    print("population", item['population'])

  option = input("Do you want to continue using program or exit? (y/n) ")
  while not validP(option):
    print("That is not a valid selection")
    option = input("Do you want to continue using program or exit? (y/n) ")
  if option == "y":
    began()
  elif option == "n":
    print("Thank you for using the program!")

def fourPl():
  num = 0
  while num <= 9:
    if num >= 0 and num <= 10:
      url = ('http://swapi.co/api/planets/?page=4')
      r = requests.get(url)
      response_dict = r.json()
      repo_dicts = response_dict['results']
      repo_dict = repo_dicts[num]['name']
      print(str(num) + " " + repo_dict)
      num += 1 

  print("If you do not see your planet please enter -1 to go back to the main starship menu")
  choice = int(input("Which one do you want to look at: "))
  if choice == -1:
    starship()
  print("Here is the information on the you wanted to see: ")

  items = []
  item = {
    "name": response_dict['results'][choice]['name'],
    "rotation_period": response_dict['results'][choice]['rotation_period'],
    "orbital_period": response_dict['results'][choice]['orbital_period'],
    "diameter": response_dict['results'][choice]['diameter'],
    "climate": response_dict['results'][choice]['climate'],
    "gravity": response_dict['results'][choice]['gravity'],
    "terrain": response_dict['results'][choice]['terrain'],
    "surface_water": response_dict['results'][choice]['surface_water'],
    "population": response_dict['results'][choice]['population']
  }

  items.append(item)

  for item in items:
    print("name:", item['name'])
    print("rotation_period:", item['rotation_period'])
    print("orbital_period:", item['orbital_period'])
    print("diameter", item['diameter'])
    print("climate", item['climate'])
    print("gravity", item['gravity'])
    print("terrain", item['terrain'])
    print("surface_water", item['surface_water'])
    print("population", item['population'])

  option = input("Do you want to continue using program or exit? (y/n) ")
  while not validP(option):
    print("That is not a valid selection")
    option = input("Do you want to continue using program or exit? (y/n) ")
  if option == "y":
    began()
  elif option == "n":
    print("Thank you for using the program!")

def fivePl():
  num = 0
  while num <= 9:
    if num >= 0 and num <= 10:
      url = ('http://swapi.co/api/planets/?page=5')
      r = requests.get(url)
      response_dict = r.json()
      repo_dicts = response_dict['results']
      repo_dict = repo_dicts[num]['name']
      print(str(num) + " " + repo_dict)
      num += 1 

  print("If you do not see your planet please enter -1 to go back to the main starship menu")
  choice = int(input("Which one do you want to look at: "))
  if choice == -1:
    starship()
  print("Here is the information on the you wanted to see: ")

  items = []
  item = {
    "name": response_dict['results'][choice]['name'],
    "rotation_period": response_dict['results'][choice]['rotation_period'],
    "orbital_period": response_dict['results'][choice]['orbital_period'],
    "diameter": response_dict['results'][choice]['diameter'],
    "climate": response_dict['results'][choice]['climate'],
    "gravity": response_dict['results'][choice]['gravity'],
    "terrain": response_dict['results'][choice]['terrain'],
    "surface_water": response_dict['results'][choice]['surface_water'],
    "population": response_dict['results'][choice]['population']
  }

  items.append(item)

  for item in items:
    print("name:", item['name'])
    print("rotation_period:", item['rotation_period'])
    print("orbital_period:", item['orbital_period'])
    print("diameter", item['diameter'])
    print("climate", item['climate'])
    print("gravity", item['gravity'])
    print("terrain", item['terrain'])
    print("surface_water", item['surface_water'])
    print("population", item['population'])

  option = input("Do you want to continue using program or exit? (y/n) ")
  while not validP(option):
    print("That is not a valid selection")
    option = input("Do you want to continue using program or exit? (y/n) ")
  if option == "y":
    began()
  elif option == "n":
    print("Thank you for using the program!")

def sixPl():
  num = 0
  while num <= 9:
    if num >= 0 and num <= 10:
      url = ('http://swapi.co/api/planets/?page=6')
      r = requests.get(url)
      response_dict = r.json()
      repo_dicts = response_dict['results']
      repo_dict = repo_dicts[num]['name']
      print(str(num) + " " + repo_dict)
      num += 1 

  print("If you do not see your planet please enter -1 to go back to the main starship menu")
  choice = int(input("Which one do you want to look at: "))
  if choice == -1:
    starship()
  print("Here is the information on the you wanted to see: ")

  items = []
  item = {
    "name": response_dict['results'][choice]['name'],
    "rotation_period": response_dict['results'][choice]['rotation_period'],
    "orbital_period": response_dict['results'][choice]['orbital_period'],
    "diameter": response_dict['results'][choice]['diameter'],
    "climate": response_dict['results'][choice]['climate'],
    "gravity": response_dict['results'][choice]['gravity'],
    "terrain": response_dict['results'][choice]['terrain'],
    "surface_water": response_dict['results'][choice]['surface_water'],
    "population": response_dict['results'][choice]['population']
  }

  items.append(item)

  for item in items:
    print("name:", item['name'])
    print("rotation_period:", item['rotation_period'])
    print("orbital_period:", item['orbital_period'])
    print("diameter", item['diameter'])
    print("climate", item['climate'])
    print("gravity", item['gravity'])
    print("terrain", item['terrain'])
    print("surface_water", item['surface_water'])
    print("population", item['population'])

  option = input("Do you want to continue using program or exit? (y/n) ")
  while not validP(option):
    print("That is not a valid selection")
    option = input("Do you want to continue using program or exit? (y/n) ")
  if option == "y":
    began()
  elif option == "n":
    print("Thank you for using the program!")

def sevenPl():
  num = 0
  while num < 1:
    if num >= 0 and num < 1:
      url = ('http://swapi.co/api/planets/?page=7')
      r = requests.get(url)
      response_dict = r.json()
      repo_dicts = response_dict['results']
      repo_dict = repo_dicts[num]['name']
      print(str(num) + " " + repo_dict)
      num += 1 

  print("If you do not see your planet please enter -1 to go back to the main starship menu")
  choice = int(input("Which one do you want to look at: "))
  if choice == -1:
    starship()
  print("Here is the information on the you wanted to see: ")

  items = []
  item = {
    "name": response_dict['results'][choice]['name'],
    "rotation_period": response_dict['results'][choice]['rotation_period'],
    "orbital_period": response_dict['results'][choice]['orbital_period'],
    "diameter": response_dict['results'][choice]['diameter'],
    "climate": response_dict['results'][choice]['climate'],
    "gravity": response_dict['results'][choice]['gravity'],
    "terrain": response_dict['results'][choice]['terrain'],
    "surface_water": response_dict['results'][choice]['surface_water'],
    "population": response_dict['results'][choice]['population']
  }

  items.append(item)

  for item in items:
    print("name:", item['name'])
    print("rotation_period:", item['rotation_period'])
    print("orbital_period:", item['orbital_period'])
    print("diameter", item['diameter'])
    print("climate", item['climate'])
    print("gravity", item['gravity'])
    print("terrain", item['terrain'])
    print("surface_water", item['surface_water'])
    print("population", item['population'])

  option = input("Do you want to continue using program or exit? (y/n) ")
  while not validP(option):
    print("That is not a valid selection")
    option = input("Do you want to continue using program or exit? (y/n) ")
  if option == "y":
    began()
  elif option == "n":
    print("Thank you for using the program!")

############# END OF PLANETS #####################

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

################ START OF SPECIES #############

def species():
  print("Here you will find information about Species in Star Wars")
  print("There are a lot of species which will be in groups of 10.")
  print("Please choose which group you want to look at:")
  print("1: First Group")
  print("2: Second Group")
  print("3: Third Group")
  print("4: Fourth Group")
  choice = int(input("What do you want to look at: "))
  if choice == 1:
    oneSP()
  elif choice == 2:
    twoSP()
  elif choice == 3:
    threeSP()
  elif choice == 4:
    fourSP()

def oneSP():
  num = 0
  while num < 9:
    if num >= 0 and num <= 10:
      url = ('http://swapi.co/api/species/')
      r = requests.get(url)
      response_dict = r.json()
      repo_dicts = response_dict['results']
      repo_dict = repo_dicts[num]['name']
      print(str(num) + " " + repo_dict)
      num += 1 

  print("If you do not see your planet please enter -1 to go back to the main starship menu")
  choice = int(input("Which one do you want to look at: "))
  if choice == -1:
    starship()
  print("Here is the information on the you wanted to see: ")

  items = []
  item = {
    "name": response_dict['results'][choice]['name'],
    "classification": response_dict['results'][choice]['classification'],
    "designation": response_dict['results'][choice]['designation'],
    "average_height": response_dict['results'][choice]['average_height'],
    "skin_colors": response_dict['results'][choice]['skin_colors'],
    "hair_colors": response_dict['results'][choice]['hair_colors'],
    "eye_colors": response_dict['results'][choice]['eye_colors'],
    "average_lifespan": response_dict['results'][choice]['average_lifespan'],
    "language": response_dict['results'][choice]['language']
  }

  items.append(item)

  for item in items:
    print("name:", item['name'])
    print("classification", item['classification'])
    print("designation", item['designation'])
    print("average_height", item['average_height'])
    print("skin_colors", item['skin_colors'])
    print("hair_colors", item['hair_colors'])
    print("eye_colors", item['eye_colors'])
    print("average_lifespan", item['average_lifespan'])
    print("language", item['language'])

  option = input("Do you want to continue using program or exit? (y/n) ")
  while not validP(option):
    print("That is not a valid selection")
    option = input("Do you want to continue using program or exit? (y/n) ")
  if option == "y":
    began()
  elif option == "n":
    print("Thank you for using the program!")

def twoSP():
  num = 0
  while num < 9:
    if num >= 0 and num <= 10:
      url = ('http://swapi.co/api/species/?page=2')
      r = requests.get(url)
      response_dict = r.json()
      repo_dicts = response_dict['results']
      repo_dict = repo_dicts[num]['name']
      print(str(num) + " " + repo_dict)
      num += 1 

  print("If you do not see your planet please enter -1 to go back to the main starship menu")
  choice = int(input("Which one do you want to look at: "))
  if choice == -1:
    starship()
  print("Here is the information on the you wanted to see: ")

  items = []
  item = {
    "name": response_dict['results'][choice]['name'],
    "classification": response_dict['results'][choice]['classification'],
    "designation": response_dict['results'][choice]['designation'],
    "average_height": response_dict['results'][choice]['average_height'],
    "skin_colors": response_dict['results'][choice]['skin_colors'],
    "hair_colors": response_dict['results'][choice]['hair_colors'],
    "eye_colors": response_dict['results'][choice]['eye_colors'],
    "average_lifespan": response_dict['results'][choice]['average_lifespan'],
    "language": response_dict['results'][choice]['language']
  }

  items.append(item)

  for item in items:
    print("name:", item['name'])
    print("classification", item['classification'])
    print("designation", item['designation'])
    print("average_height", item['average_height'])
    print("skin_colors", item['skin_colors'])
    print("hair_colors", item['hair_colors'])
    print("eye_colors", item['eye_colors'])
    print("average_lifespan", item['average_lifespan'])
    print("language", item['language'])

  option = input("Do you want to continue using program or exit? (y/n) ")
  while not validP(option):
    print("That is not a valid selection")
    option = input("Do you want to continue using program or exit? (y/n) ")
  if option == "y":
    began()
  elif option == "n":
    print("Thank you for using the program!")

def threeSP():
  num = 0
  while num < 9:
    if num >= 0 and num <= 10:
      url = ('http://swapi.co/api/species/?page=3')
      r = requests.get(url)
      response_dict = r.json()
      repo_dicts = response_dict['results']
      repo_dict = repo_dicts[num]['name']
      print(str(num) + " " + repo_dict)
      num += 1 

  print("If you do not see your planet please enter -1 to go back to the main starship menu")
  choice = int(input("Which one do you want to look at: "))
  if choice == -1:
    starship()
  print("Here is the information on the you wanted to see: ")

  items = []
  item = {
    "name": response_dict['results'][choice]['name'],
    "classification": response_dict['results'][choice]['classification'],
    "designation": response_dict['results'][choice]['designation'],
    "average_height": response_dict['results'][choice]['average_height'],
    "skin_colors": response_dict['results'][choice]['skin_colors'],
    "hair_colors": response_dict['results'][choice]['hair_colors'],
    "eye_colors": response_dict['results'][choice]['eye_colors'],
    "average_lifespan": response_dict['results'][choice]['average_lifespan'],
    "language": response_dict['results'][choice]['language']
  }

  items.append(item)

  for item in items:
    print("name:", item['name'])
    print("classification", item['classification'])
    print("designation", item['designation'])
    print("average_height", item['average_height'])
    print("skin_colors", item['skin_colors'])
    print("hair_colors", item['hair_colors'])
    print("eye_colors", item['eye_colors'])
    print("average_lifespan", item['average_lifespan'])
    print("language", item['language'])

  option = input("Do you want to continue using program or exit? (y/n) ")
  while not validP(option):
    print("That is not a valid selection")
    option = input("Do you want to continue using program or exit? (y/n) ")
  if option == "y":
    began()
  elif option == "n":
    print("Thank you for using the program!")

def fourSP():
  num = 0
  while num < 7:
    if num >= 0 and num <= 7:
      url = ('http://swapi.co/api/species/?page=4')
      r = requests.get(url)
      response_dict = r.json()
      repo_dicts = response_dict['results']
      repo_dict = repo_dicts[num]['name']
      print(str(num) + " " + repo_dict)
      num += 1 

  print("If you do not see your planet please enter -1 to go back to the main starship menu")
  choice = int(input("Which one do you want to look at: "))
  if choice == -1:
    starship()
  print("Here is the information on the you wanted to see: ")

  items = []
  item = {
    "name": response_dict['results'][choice]['name'],
    "classification": response_dict['results'][choice]['classification'],
    "designation": response_dict['results'][choice]['designation'],
    "average_height": response_dict['results'][choice]['average_height'],
    "skin_colors": response_dict['results'][choice]['skin_colors'],
    "hair_colors": response_dict['results'][choice]['hair_colors'],
    "eye_colors": response_dict['results'][choice]['eye_colors'],
    "average_lifespan": response_dict['results'][choice]['average_lifespan'],
    "language": response_dict['results'][choice]['language']
  }

  items.append(item)

  for item in items:
    print("name:", item['name'])
    print("classification", item['classification'])
    print("designation", item['designation'])
    print("average_height", item['average_height'])
    print("skin_colors", item['skin_colors'])
    print("hair_colors", item['hair_colors'])
    print("eye_colors", item['eye_colors'])
    print("average_lifespan", item['average_lifespan'])
    print("language", item['language'])

  option = input("Do you want to continue using program or exit? (y/n) ")
  while not validP(option):
    print("That is not a valid selection")
    option = input("Do you want to continue using program or exit? (y/n) ")
  if option == "y":
    began()
  elif option == "n":
    print("Thank you for using the program!")



################ END OF SPECIES #############

################ START OF VEHICLES #############





################ END OF VEHICLES #############


################ START OF STARSHIPS #############

def starship():
  print("Here you will find information about Starships in Star Wars")
  print("There are a lot of ships which will be in groups of 10.")
  print("Please choose which group you want to look at:")
  print("1: First Group")
  print("2: Second Group")
  print("3: Third Group")
  print("3: Fourth Group")
  choice = int(input("What do you want to look at: "))
  if choice == 1:
    one()
  elif choice == 2:
    two()
  elif choice == 3:
    three()
  elif choice == 4:
    four()

def one():
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
    people()
  elif choice == 2:
    planets()
  elif choice == 3:
    films()
  elif choice == 4:
    species()
  elif choice == 6:
    starship()

############ Valid Functions ############
### These Function will ensure that user input is correct. 

def valid(choice):
  if choice == "y" or choice == "n":
    return True 
  else:
    return False 

def validP(option):
  if option == "y" or option == "n":
    return True 
  else:
    return False 
  


#This function starts the program and basically asks the user if
#they want to use it. 
def main():
  print('*******************')
  print('---STAR WARS API--- ')
  print('*******************')
  choice = input("Would you like to use it?(y/n) ")
  while not valid(choice):
    print("That is not a valid selection")
    choice = input("Would you like to use it?(y/n) ")
  if choice.lower() == "y":
    began()
  else:
    print("Hope you use it soon!")

main()

#This program will use the http://swapi.co/api/ api which will allow the user to look at
#star wars data. 

import requests 


def began():
  print("To start, Here are the categories you can look at:")
  print("people")
  print("planets")
  print("films")
  print("species")
  print("vehicles")
  print("starships")
  view = input("What do you want to look at?")


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
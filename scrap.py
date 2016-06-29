
#Process the results
# print(response_dict.keys())

#printing information about the API:
#Here I show that the API has a count of 37 objects. 
# print("Total Starships: ", response_dict['count'])

#Here I am showing what the ship in element 1 is. 
#print(response_dict['results'][1])

#Exploring information about the repositories.
repo_dicts = response_dict['results']
# print("repositories returned:", len(repo_dicts))

#Examine the first repo
repo_dict = repo_dicts[1]
print("Keys:", len(repo_dict))
#I will be able to see what data is available about each starship now. 
for key in sorted(repo_dict.keys()):
  print(key)

# print("\nSelected information about the Second starship:")
# print("Name:", repo_dict['name'])
# print("Crew: ", repo_dict['crew'])
# print("max_atmosphering_speed:", repo_dict['max_atmosphering_speed'])

###Collecting information about more than one repo
print("\nSelected information about each repo:")

#Creating two empty list to hold the names and crew data.
# names, crew = [], []
#I loop through the api and then print out each name and crew of each ship. 
# for repo_dict in repo_dicts:
  # print("\nName:", repo_dict['name'])
  # print("Crew: ", repo_dict['crew'])
  #Appending the data to the names and crew list 
  # names.append(repo_dict['name'])
  # crew.append(int(repo_dict['crew']))

#Making the visualization 
# my_style = LS('#333366', base_style=LCS)
# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
# chart.title = "Star Wars Ships and crew"
# chart.x_labels = names

# chart.add('', crew)
# chart.render_to_file('starwars.svg')
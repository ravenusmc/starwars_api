
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



#############

Star Wars API 

0 Sentinel-class landing craft         1
1 Death Star                           2
2 Millennium Falcon                    3
3 Y-wing                               4
4 X-wing                               5
5 TIE Advanced x1                      6
6 Executor                             7
7 Slave 11                             8
8 Imperial shuttle                     9
9 EF76 Nebulon-B escort frigate        10

10 status_code, page 2 200             11
11 status_code, page 2 200             12
12 status_code, page 2 200             13
13 status_code, page 2 200             14
14 status_code, page 2 200             15
15 status_code, page 2 200             16
16 status_code, page 2 200             17
17 status_code, page 2 200             18
18 status_code, page 2 200             19

19 status_code, page 3 200
20 status_code, page 3 200
21 status_code, page 3 200
22 status_code, page 3 200
23 status_code, page 3 200
24 status_code, page 3 200
25 status_code, page 3 200
26 status_code, page 3 200
27 status_code, page 3 200
28 status_code, page 3 200

29 status_code, page 4 200
30 status_code, page 4 200
31 status_code, page 4 200
32 status_code, page 4 200
33 status_code, page 4 200
34 status_code, page 4 200
35 status_code, page 4 200
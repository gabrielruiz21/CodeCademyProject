#This program could be implemented on a travel agency. This whole program will recommend user attractions to visit according to the place they want to go and their interests.
#destinations and test traveler are just for testing purposes. In the future i would like to gather this information from an API or the user's profile.

#this list contains some famous destinations
destination = ['Paris, France','Shanghai, China', 'Los Angeles, USA','Sao Paulo, Brazil','Cairo, Egypt']

#this list will be populated with the recommended attractios the user should visit according to his interest and his destination.
attractions_with_interest = []

#I will be using this list to recommend the user attractions accroding to his interests.
attractions = [[], [], [], [], []]

#the objective of this class is to make the proccess of adding destinations and attraction to the attraction list.
def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions [destination_index]
    attractions_for_destination.append(attraction)
  except ValueError:
    return 0

#this function will just gather the destination index which will be use to find the attractions on it.
def get_destination_index(name):
    destination_index = destination.index(name)
    return destination_index

#this will gather the users's destination to visit and associate with our destination list
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

#this function is in charge of looping throught the attractions list and compare where the attractions in the user's destination match his interests.
def find_attractions(destination,interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  possible_attraction = ""
  attraction_tags = ""
  for items in attractions_in_city:
    possible_attraction = items
    attraction_tags = items[1]
    for tags in attraction_tags:
      if tags in interests:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest


#This function is the main. This will use the previous functions, collect the data and present it to the user in a friendly way.
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination,traveler_interests)
  interests_string = "Good choice " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": "
  for item in traveler_attractions:
    interests_string += item + ", "

  return interests_string

#This lines are just so i can populate the attractions list with real data.
add_attraction("Los Angeles, USA",['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["Sao Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Patio do Colegio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])


#here i am using a user data so i can test the program. You will fin the user's name, folow by the place he wants to go and his interests.
user_name = input("Hello there, thanks for chosing us for your next adventure. Let's know each other firt. What is your name:   ")
print(f'It is nice to meet you {user_name}, Here is a list of attractions you might be interested on {destination}')
user_destination = input("Which one you fancy the most ?  ")
user_interests = input("Lasly, what are your interests? \n beach,art,museum,historical site,monument,garden,skyscraper,viewing deck \n")
user_interests = user_interests.split(',')
# print(user_interests)
smills_france = get_attractions_for_traveler([user_name, user_destination, user_interests])
print(smills_france)
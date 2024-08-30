my_dictionary = {
  "Miller" : "a person who owns or works in a corn mill", 
  "Programmer" : "a person who writes computer programs",
  "App" : "an application, especially as downloaded by a user to a mobile device",
  }

# Loop Through

for key in my_dictionary:
  print(key, my_dictionary[key])

# Search
for key in my_dictionary:
  if key == "Appp":
      print("It exists in the dictionary")
      print(my_dictionary[key])
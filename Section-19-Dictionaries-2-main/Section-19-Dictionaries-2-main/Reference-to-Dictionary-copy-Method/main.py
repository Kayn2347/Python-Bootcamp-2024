name_list = ["Kayn", "Dhea", "Chisee"]
city_list = ["London", "Berlin", "Paris"]
language_list = ["Enlish", "German", "French"]

person = {
    "name" : name_list,
    "city" : city_list,
    "language" : language_list,
}

new_person = person.copy()
person["city"].append("Appended using person dict")
new_person["city"].append("Appended using new person dict")
city_list.append("Append by itself")
print(person["city"])
print(new_person["city"])
print(city_list)

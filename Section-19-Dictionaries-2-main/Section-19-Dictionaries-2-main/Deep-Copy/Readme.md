import copy
city_list = ["London", "Berlin", "Paris"]
language_list = ["English", "German", "French"]
name_list = ["Kayn", "Dhea", "Chisee"]
person = {
    "name" : name_list,
    "city" : city_list,
    "language" : language_list,
}

# new_person = person.copy()
# Deep copy
new_person = copy.deepcopy(person)
new_person["city"].append("Madrid")
# print(new_person["city"])
# print(person["city"])
print(id(new_person["city"]), new_person["city"])
print(id(person["city"]), person["city"])


def deep_copy(p_dict):
  new_dict = {}
  for key, value in p_dict.items():
      new_value = value.copy()
      new_dict[key] = new_value
  return new_dict

original_dict = {
  "names" : ["Kayn", "Dhea", "Chisee"],
  "numbers" : [1,2,3,4,5]
}

copied_dict = deep_copy(original_dict)
copied_dict["names"].append("Jack")
copied_dict["numbers"].append(6)

print(original_dict)
print(copied_dict)



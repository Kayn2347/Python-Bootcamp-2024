names_dict = {
  1 : "Kayn",
  2 : "Heart",
  3 : "Dhea",
  4 : "Appmillers"
}

def value_length(p_dict):
  output_dict = {}
  for key, value in p_dict.items():
      output_dict[key] = {}
      output_dict[key][value] = len(value)
  return output_dict

print(value_length(names_dict))

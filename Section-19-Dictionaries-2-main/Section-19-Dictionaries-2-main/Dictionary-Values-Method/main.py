custom_dict = {
  0 : "zero",
  1 : "one",
  2 : "two",
  3 : "three",
  4 : "four",
  5 : "five",
  6 : "six",
  7 : "seven",
  "v" : "five",
}


values = list(custom_dict.values())
keys = list(custom_dict.keys())
if "five" in values:
  index = values.index("five")
  key = keys[index]
  print(f"{custom_dict[key]} is found with the key {key}")

print()
for key, value in custom_dict.items():
  if value == "five":
     print(f"{custom_dict[key]} is found with the key {key}") 

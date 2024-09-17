general_items = {
  "Sand toys",
  "Beach towels",
  "Beach umbrella",
  "Camp chair",
  "Snacks",
  "Hats",
  "Camera",
  "Sunglasses",
  "Alcoholic Drinks",
  "Non Alcoholic Drinks",
  "Cigarettes",
  "Sharp Objects"
}

restricted_items = {
  "Non Alcoholic Drinks",
  "Sigarettes",
  "Sharp Objects",
  "Amplified Audio",
  "Drugs"
  }

user_input = input("Select Beach Type (1 - Family beach, 2 - Normal Beach):  ")
if user_input == "1":
  for item in restricted_items:
      general_items.discard(item)
else:
  general_items.discard("Drugs")
print("See below the list of items that you can take.")
for item in general_items:
  print(f"\t{item}")
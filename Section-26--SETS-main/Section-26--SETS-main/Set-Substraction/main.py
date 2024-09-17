fruits = {"apple", "orange", "cucumber", "grape", "pear", "limon"}
vegetables = {"cucumber", "onion", "garlic", "pepper", "broccoli"}

# Delete restricted items
general_items = {
    "Sand toys",
    "Beach towels",
    "Beach umbrella",
    "Camp chair",
    "Snacks",
    "Hats",
    "Camera",
    "Sunglasses",
    "Alcholic Drinks",
    "Non Alcholic Drinks",
    "Sigarettes",
    "Sharp Objects"
}

restricted_items = {
    "Non Alcholic Drinks",
    "Sigarettes",
    "Sharp Objects",
    "Amplified Audio",
    "Drugs"
    }

user_input = input("Select Beach Type (1 - Family beach, 2 - Normal beach): ")

if user_input == "1":
    general_items = general_items - restricted_items

else:
    general_items.discard("Drugs")

print("See below the list of items that you can take.")
for item in general_items:
    print(f"\t{item}")





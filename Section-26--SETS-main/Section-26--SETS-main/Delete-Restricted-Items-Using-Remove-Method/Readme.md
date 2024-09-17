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

user_input = input("Select Beach Type (1 - Family beach, 2 - Normal Beach):  ")
if user_input == "1":
    for item in restricted_items:
        try:
            general_items.remove(item)
        except KeyError:
            print(f"skipping {item}..")
            continue
else:
    try:
        general_items.remove("Drugs")
    except:
        print(f"skipping Drugs..")
print("See below the list of items that you can take.")
for item in general_items:
    print(f"\t{item}")




available_parts = {
    "1": "computer",
    "2": "monitor",
    "3": "keyboard",
    "4": "mouse",
    "5": "hdmi cable",
    "6": "dvd drive",
}

price_quantity = {
    "computer": {"price": 500, "quantity" : 10},
    "monitor": {"price": 200, "quantity" : 8},
    "keyboard": {"price": 500, "quantity" : 5},
    "mouse": {"price": 10, "quantity" : 0},
    "hdmi cable": {"price": 20, "quantity" : 7},
    "dvd drive": {"price": 50, "quantity" : 5},
}

# print("Please add options from the list:")
# for key, value in available_parts.items():
#     print(f"{key}: {value}")
# print("0: to finish")



current_choice = None
total_price = 0

while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if price_quantity[chosen_part]["quantity"] > 0:
            print(f"Adding {chosen_part}")
            price_quantity[chosen_part]["quantity"] -= 1
            total_price += price_quantity[chosen_part] ["price"]

        else:
              print(f"{chosen_part} is out of stock!")
    else:
         print("Please add options from the list")
         for key, value in available_parts.items():
             print(f"{key}: {value}")
         print("0: to finish")

    current_choice = input("> ")

print(f"Total price: {total_price}")
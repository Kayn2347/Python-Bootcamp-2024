age = 26

def select_drink():
    drink_types = ["alcoholic", "non-alcoholic"]
    if age < 18:
        drink_type = drink_types[1]

    print(drink_types)

select_drink()
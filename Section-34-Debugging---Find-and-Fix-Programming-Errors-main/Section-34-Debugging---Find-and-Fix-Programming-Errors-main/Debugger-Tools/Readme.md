# Using Debugger Tools

deck_cards = ["Heart", "Dimond", "Spade", "Club"]

def custom_function(a_list):
    result_list = []
    for item in a_list:
        new_item = item + "s"
    result_list.append(new_item)
    return result_list

print(custom_function(deck_cards))
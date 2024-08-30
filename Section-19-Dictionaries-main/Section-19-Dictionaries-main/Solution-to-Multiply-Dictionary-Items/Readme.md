my_dict = {"One" : 1, "Two" : 2, "Three" : 3, "Four" : 4}
def multiply_values(p_dict):
    output = 1
    for key in p_dict:
        output = output * p_dict[key]
    return output

print(multiply_values(my_dict))

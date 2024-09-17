my_tuple = (1,2,3,4,5,6,7)

def search_tuple(p_tuple, p_item):
    for index, value in enumerate(p_tuple):
        if value == p_item:
            return index
    return "The item does not exist"

result = search_tuple(my_tuple, 8)
print(result)
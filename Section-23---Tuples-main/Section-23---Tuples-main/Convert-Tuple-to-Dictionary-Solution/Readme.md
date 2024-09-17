def convert_to_dict(tup):
    result_dict = {}
    for x, y in tup:
       result_dict.setdefault(x, y)
    return result_dict


my_tuple = [("one", 1), ("two", 2), ("three", 3), ("four", 4)]

print(convert_to_dict(my_tuple))

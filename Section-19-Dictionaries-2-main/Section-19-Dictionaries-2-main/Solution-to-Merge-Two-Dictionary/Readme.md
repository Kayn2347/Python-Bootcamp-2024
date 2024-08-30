dict1 = {'One': 2, 'Two': 2, 'Three': 3}
dict2 = {'Three': 3, 'Four': 4, 'Five': 5}

def merge_dict(p_dict1, p_dict2):
    dict3 = p_dict1.copy()
    dict3.update(p_dict2)
    return dict3

print(merge_dict(dict1, dict2))
print(dict1)
print(dict2)


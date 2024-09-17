def sum_list(p_List):
    if not isinstance(p_List, list):
        return -1
    elif len(p_List) == 1:
        return p_List[0]
    else:
        total = p_List[0] + sum_list(p_List[1:])
        return total

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))
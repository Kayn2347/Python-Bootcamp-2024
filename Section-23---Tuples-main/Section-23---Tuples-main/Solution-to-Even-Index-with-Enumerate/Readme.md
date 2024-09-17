def even_index_items(p_tuple):
    result_list = []
    for index, value in enumerate(p_tuple):
        if not index % 2:
            result_list.append(value)
    result_tuple = tuple(result_list)
    return result_tuple

my_tuple = ("a", "b", "c", "d", "e", "f", "g")
result = even_index_items(my_tuple)
print(result)
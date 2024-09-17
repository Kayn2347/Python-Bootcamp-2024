my_list = [3,4,5,1,1,3,4,9,8]

def adding_set(p_list):
    result_set = set()
    for item in p_list:
        result_set.add(item)
    return result_set

print(adding_set(my_list))
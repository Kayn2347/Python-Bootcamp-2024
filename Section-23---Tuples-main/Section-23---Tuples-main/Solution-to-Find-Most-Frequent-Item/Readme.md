my_tuple = ("a","b","c","d","e","a","c","e","b","e","c","a","f","e","r")

def most_frequent(p_tuple):
    v_count = 0
    item = p_tuple[0]
    for value in p_tuple:
        current_item_count = p_tuple.count(value)
        if current_item_count > v_count:
            v_count = current_item_count
            item = value
    return (item, v_count)
    # return {"item" : item, "frequency" : v_count}

print(most_frequent(my_tuple))

list_of_sets = [
    {10,20,30,40,50},
    {"apple", "orange","limon","pear"},
    {"London", "Berlin", "Paris"},
    {"Python", "Java", "Swift"},
    {10, "ten", "20", 20}
]
def convert_ls(p_ls):
    final_set = set()
    for item in p_ls:
        final_set = final_set.union(item)
    return final_set

print(convert_ls(list_of_sets))
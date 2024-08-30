list_one = [4, 12, 16, 21, 24, 28, 32]

list_two = [5, 10, 15, 20, 25, 30, 35]

third_list = list()

odd_elements = list_one[1::2]
even_elements = list_two[0::2]
third_list.extend(odd_elements)
third_list.extend(even_elements)
print(third_list)

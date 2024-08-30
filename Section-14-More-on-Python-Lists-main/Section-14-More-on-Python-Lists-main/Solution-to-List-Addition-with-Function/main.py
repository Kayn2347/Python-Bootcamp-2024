def custom_insert(p_list, value):
  copy_list = p_list[:]
  copy_list.append(value)
  return copy_list

list1 = [1,2,3,4,5]
list2 = custom_insert(list1, 6)
print(list1)
print(list2)
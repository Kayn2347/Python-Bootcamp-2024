def concatenate(p_list1, p_list2):
  list3 = []
  for item1 in p_list1:
      for item2 in p_list2:
          list3.append(item1 + item2)
  return list3

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
print(concatenate(list1, list2))
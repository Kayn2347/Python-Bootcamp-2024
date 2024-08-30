def square_list(p_list):
  for index in range(len(p_list)):
      p_list[index] = p_list[index] * p_list[index]
  return p_list

custom_list = [1,2,3,4,5,6,7,8,9,10]
print(square_list(custom_list))
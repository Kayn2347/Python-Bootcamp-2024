def generate_dictionary(n):
  my_dict = dict()
  for num in range(1,n+1):
      my_dict[num] = num * num
  return my_dict

output = generate_dictionary(7)
print(output)
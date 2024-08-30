
custom_list = [1, 2, 3, 4, 5]
output_list = []

for item in custom_list:
    output_list.append(str(item))

custom_string = " | ".join(output_list)
print(custom_string)
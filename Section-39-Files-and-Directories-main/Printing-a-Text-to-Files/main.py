# with open("sample1.txt", "w") as file:
#     for i in range(11):
#         content = f"{i}\n"
#         file.write(content)


# with open("sample2.txt", "a") as file:
#     for i in range(11, 29):
#         content = f"{i}\n"
#         file.write(content)

with open("sample_print.txt", 'w') as sample_file:
    for i in range(11):
         print(i, file=sample_file)

with open("sample_print.txt", 'w') as file:
    for element in file:
         print(element, end="")

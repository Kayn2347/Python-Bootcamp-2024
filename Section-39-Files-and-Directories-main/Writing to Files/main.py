with open("sample1.txt", "w") as file:
    for i in range(11):
        content = f"{i}\n"
        file.write(content)


with open("sample2.txt", "a") as file:
    for i in range(11, 29):
        content = f"{i}\n"
        file.write(content)

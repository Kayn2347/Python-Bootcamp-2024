new_string = input("Enter a string: ")
index = -1
length = -1 * len(new_string)

while index >= length:
    letter = new_string[index]
    print(letter)
    index -= 1
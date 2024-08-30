def count_letter(word, letter):
    counter = 0
    for char in word:
        if char == letter:
            counter += 1
    return counter

print(count_letter("Computer", "n"))
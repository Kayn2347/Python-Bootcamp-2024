def add_odd_numbers():
    total = 0
    for number in range(1, 101, 2):
        total += number
    return total

print(add_odd_numbers())
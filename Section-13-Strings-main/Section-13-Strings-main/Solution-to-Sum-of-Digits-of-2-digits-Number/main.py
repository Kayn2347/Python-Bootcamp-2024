def sum_of_two_digits():
    two_digit_number = input("Enter two digit number: ")
    sum_of_digits = int(two_digit_number[0]) + int(two_digit_number[1])
    return sum_of_digits

print(sum_of_two_digit())
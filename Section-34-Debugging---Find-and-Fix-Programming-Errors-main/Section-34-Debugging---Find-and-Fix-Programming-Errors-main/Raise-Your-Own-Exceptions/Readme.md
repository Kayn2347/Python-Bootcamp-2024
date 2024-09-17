# while True:
#     number = input("Enter a number: ")
#     sum_of_digits = 0
#     try:
#         for digit in number:
#             sum_of_digits += int(digit)
#     except ValueError:
#         print("This value is not numeric!")
#     else:
#         print(f"Sum of digits: {sum_of_digits}")
#     finally:
#         raise TypeError("This is the error that I made up")

working_hours = float(input("Working hours:"))
rate = float(input("Rate per hour:"))
if working_hours > 40:
    raise ValueError("Working hours cannot be more than 40 weekly!")
total_pay = working_hours * rate
print(total_pay)
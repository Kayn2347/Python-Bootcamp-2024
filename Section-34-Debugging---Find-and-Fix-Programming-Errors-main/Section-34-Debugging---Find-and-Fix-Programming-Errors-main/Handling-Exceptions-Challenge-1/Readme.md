while True:
number = input("Enter a number:")
sum_of_digits = 0
try:
   for digit in number:
       sum_of_digits += int(digit)
except ValueError:
  print("This value is not numeric!")
else:
    print(f"Sum of digits: {sum_of_digits}")
finally:
    break
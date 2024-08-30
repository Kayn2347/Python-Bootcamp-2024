import random 
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
symbols = "-+=!@#$%^&*"
number_of_letters = int(input("How many letters do you want in your password? "))
number_of_numbers = int(input("How many numbers do you want in your password? "))
number_of_symbols = int(input("How many symbols do you want in your password? "))


password = ""

for char in range(1, number_of_letters + 1):
  password += random.choice(letters)

for num in range(1, number_of_numbers + 1):
  password += random.choice(nums)

for symbol in range(1, number_of_symbols + 1):
  password += random.choice(symbols)

print(password)
print(f"Your password is: {password}")

# more advances
password_list = list(password)
random.shuffle(password_list)
print(password_list)
password = ""
for p in password_list:
    password += p

print(f"Your advanced password is: {password}")
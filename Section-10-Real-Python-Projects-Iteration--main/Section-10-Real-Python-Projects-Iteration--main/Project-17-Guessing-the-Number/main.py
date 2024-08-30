import math
import random

lower = int(input("Enter Lower bound: "))
upper = int(input("Enter Upper bound: "))
number_of_chances = int(math.log(upper-lower+1,2))
print(f"\n\tYou've only {number_of_chances} chances to guess the integer!\n")

generated_number = random.randint(lower, upper)

count = 0

while count < number_of_chances:
    count += 1
    guess = int(input("Guess a number: "))
    if generated_number == guess:
        print(f"Congratulations you did it in {count} try")
        break
    elif guess > generated_number:
        print("You guessed too high!")
    elif guess < generated_number:
        print("You guessed too low!")

print(f"\nThe number is {generated_number} ")
# print("\tBetter Luck Next time!")
import random
print("Welcome to Love Calculator!")
name1 = input("Enter your name: ")
name2 = input("Enter your lover name: ")

love_score = random.randint(1,100)

if love_score < 10 or love_score > 85:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 70:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
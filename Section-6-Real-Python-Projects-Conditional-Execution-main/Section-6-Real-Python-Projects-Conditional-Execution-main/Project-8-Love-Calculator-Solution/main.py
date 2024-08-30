#Solution
print("Welcome to Love Calculator!")
name1 = input("Enter your name: ")
name2 = input("Enter your lover name: ")

combined_name = name1 + name2

lower_cased_name = combined_name.lower()

t = lower_cased_name.count("t")
r = lower_cased_name.count("r")
u = lower_cased_name.count("u")
e = lower_cased_name.count("e")

true = t + r + u + e

l = lower_cased_name.count("l")
o = lower_cased_name.count("o")
v = lower_cased_name.count("v")
e = lower_cased_name.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))
print(love_score)

if love_score < 10 or love_score > 85:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 and love_score <= 70:
    print(f"Your score is {love_score}, you alright go together")
else:
    print(f"Your score is {love_score}")

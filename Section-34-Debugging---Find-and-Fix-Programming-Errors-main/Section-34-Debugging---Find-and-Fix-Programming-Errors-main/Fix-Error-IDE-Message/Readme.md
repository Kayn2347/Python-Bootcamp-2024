 # Fix Error - IDE Message 

def custom_function(age):
    if age > 50 and age < 62:
       print("Your {age} eligible for retirement")
    elif age > 62:
        print("You are retired")

age = int(input("What is your age? "))
custom_function(age)
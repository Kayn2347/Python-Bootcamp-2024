print("Welcome to Mortagage Calculator!")
salary = int(input("What is your salary?"))

if salary >=2000:
  print("You are eligible for mortagage!")
  credit_score = int(input("What is your credit score?"))
  if credit_score > 800:
    print("Interest rate: 4%")
  elif credit_score > 750:
    print("Interest rate: 6%")
  else:
    rate = 8
    print("Interest rate: 8%")
    disability = input("Do you have any disability? Y or N")
    if disability == "Y":
      rate -=2
      print(f"Final Interest Rate: {rate}")
else:
  print("Sorry, you are not eligible!")

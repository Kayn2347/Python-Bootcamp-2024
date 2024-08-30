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
    print("Interest rate: 8%")
else:
  print("Sorry, you are not eligible!")
  
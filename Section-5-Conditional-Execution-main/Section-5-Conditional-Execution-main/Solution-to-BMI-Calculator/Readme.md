height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / height ** 2,2)

if bmi < 18.5:
    print(f"Your bmi is {bmi} , you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi} , you weight is normal.")
elif bmi < 30:
    print(f"Your bmi is {bmi} , you are overweight.")
else:
    print(f"Your bmi is {bmi} , you are obese.")
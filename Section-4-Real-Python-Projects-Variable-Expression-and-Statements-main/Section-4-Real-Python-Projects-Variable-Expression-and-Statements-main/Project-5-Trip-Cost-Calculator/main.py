# print("Welcome to the Trip Cost Calculator")
# day =input("How many days will you stay? ")
# hotel_price = input("How much does hotel cost per night? $ ")
# flight_price = input("How much does flight cost? $")
# car_price = input("If you need rental car please enter the price otherwise enter zero. $")
# other_expenses = input("Enter other possible expenses.$")

# Convert values to float or integer

print("Welcome to the Trip Cost Calculator")
day =int(input("How many days will you stay? "))
hotel_price = float(input("How much does hotel cost per night? $ "))
flight_price = float(input("How much does flight cost? $"))
car_price = float(input("If you need rental car please enter the price otherwise enter zero. $"))
other_expenses = float(input("Enter other possible expenses.$"))
total_cost = round(day * hotel_price + flight_price + day * car_price + other_expenses, 2)
print(f"Total Cost: ${total_cost}")
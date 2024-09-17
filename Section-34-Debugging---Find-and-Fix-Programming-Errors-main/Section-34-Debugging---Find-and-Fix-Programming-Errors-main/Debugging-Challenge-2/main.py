hour = input("Enter Hours: ")
rate = float(input("Enter Rate: "))


if hour < 40:
    pay = round(hour*rate,2)
else:
    overtime = hour - 40;
    pay = (rate * 40.0) + (1.5 * rate * overtime)

print(f"Pay: {pay}")
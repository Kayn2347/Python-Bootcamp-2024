

def compute_pay(p_hour, p_rate):
    if p_hour < 40:
        pay = round(p_hour*p_rate,2)
    else:
        overtime = p_hour - 40
        pay = round(40 * p_rate + overtime * p_rate * 1.5,2)
    return pay

def check_for_float(p_input):
    try:
        val = float(p_input)         
        return val
    except ValueError:
        print("Error, please enter numeric input")
        quit()

hour = input("Enter Hours: ")
hour = check_for_float(hour)
rate = input("Enter Rate: ")
rate = check_for_float(rate)

output = compute_pay(hour, rate)
print(f"Pay: {output}")
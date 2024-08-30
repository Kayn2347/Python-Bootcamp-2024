def factorial(p_num):
    factorial = 1
    if p_num < 0:
        return "Factorial does not exist for negative numbers"
    elif p_num == 0:
        return "The factorial of 0 is 1"
    else:
        for num in range(1, p_num + 1):
            factorial = factorial * num
        return f"The factorial of {p_num} is {factorial}"

print(factorial(-1))
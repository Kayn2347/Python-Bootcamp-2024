def add(n1,n2):
  return n1 + n2

def subtract(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1 / n2

n1 = int(input("What is the first number? "))
n2 = int(input("What is the second number? "))
operation = input("Pick operation from this list (+,-,*,/) ")

if operation == "+":
  answer = add(n1,n2)
elif operation == "-":
  answer = subtract(n1,n2)
elif operation == "*":
  answer = multiply(n1,n2)
elif operation == "/":
  answer = divide(n1,n2)

print(f"{n1} {operation} {n2} = {answer}")

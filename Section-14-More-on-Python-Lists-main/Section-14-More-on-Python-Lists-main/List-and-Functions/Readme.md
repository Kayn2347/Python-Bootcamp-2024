numlist =[]

while True:
    inp = input("Enter a number:")
    if inp == "done": 
        break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print(f"Average: {average}")
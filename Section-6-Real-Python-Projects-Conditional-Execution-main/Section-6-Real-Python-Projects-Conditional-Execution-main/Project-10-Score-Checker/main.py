#Solution
input_score = input("Enter score: ")
try:
    score = float(input_score)
except ValueError:
    print("Bad Score")
    quit()

if score >= 0.0 and score <= 1.0:
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")
else:
    print("Bad score")
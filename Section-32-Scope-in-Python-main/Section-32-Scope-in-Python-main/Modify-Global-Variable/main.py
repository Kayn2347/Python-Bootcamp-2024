score = 0

def increase_score():
    print(f"Score inside function {score}")
    return score + 1

score = increase_score()
print(f"Score outside function {score} ")

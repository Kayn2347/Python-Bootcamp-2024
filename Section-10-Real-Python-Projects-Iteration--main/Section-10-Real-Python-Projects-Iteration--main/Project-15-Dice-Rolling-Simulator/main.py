import random

roll_again = "Y"

while roll_again == "Y":
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print("Dice1: " + str(dice1), "\nDice2: "+ str(dice2))
    roll_again = input("Roll the dice again? (Y/N) ")
import ascii_art
import random
print(ascii_art.logo)
# Step 1 - Ask the player to enter first 5 numbers between 1 and 69

while True:
    print("Enter 5 different numbers from 1 to 69, with spaces between \neach number. (For example: 5 17 23 42 50)")
    response = input("> ")

    numbers = response.split()
    # Check that the player entered 5 things
    if len(numbers) != 5:
        print("Please enter 5 numbers, separated by spaces.")
        continue
    # Convert the strings into integers
    try:
        for i in range(5):
            numbers[i] = int(numbers[i])
    except ValueError:
        print("Please enter numbers, like 1,10 or 35")
        continue
    # Check that the numbers are between 1 and 69
    between_1_69 = True
    for item in numbers:
        if not(1<= item <= 69):
            print("The numbers must be between 1 and 69")
            between_1_69 = False
            break
    if not between_1_69:
        continue
    # Check that the numbers are unique
    if len(set(numbers)) != 5:
        print("You must enter 5 different numbers")
        continue
    break

# Step 2 - Ask the player to select the powerball between 1 to 26
while True:
    print("Enter the powerball number from 1 to 26.")
    response = input('> ')
    try:
        powerball = int(response)
    except ValueError:
        print("Please enter a number, like 1, 10 or 35")
        continue

    if not(1 <= powerball <= 26):
        print("The powerball number must be between 1 and 26")
        continue
    break

# Step 3 - Enter the number of times you want to play
while True:
    print("How many times do you want to play (Max: 1000000)? ")
    reponse = input('> ')
    #  Convert the strings into integers
    try:
        numPlays = int(reponse)
    except ValueError:
        print("Please enter a number, like 1, 10 or 35")
        continue
    #  Check that the number is between 1 and 1000000
    if not(1 <= numPlays <= 1000000):
        print("You can play between 1 and 1000000 times.")
        continue
    break

# Step 4 - Run the simulation
price = '$' + str(2 * numPlays)
print(f"It costs {price} to play {numPlays} times, but dont \nworry. I'm sure you will win it all back.")
input("Press Enter to start...")
possibleNumbers = list(range(1,70))
for i in range(numPlays):
    # Come up with lottery numbers
    random.shuffle(possibleNumbers)
    winningNumbers = possibleNumbers[0:5]
    winningPowerball = random.randint(1,26)
    # Display winning numbers
    print("The winning numbers are: ", end="")
    allWinningNumbers = ""
    for num in winningNumbers:
        allWinningNumbers += str(num) + ' '
    allWinningNumbers += "and " + str(winningPowerball)
    print(allWinningNumbers, end = "")
    #  Check for winner
    if (set(numbers) == set(winningNumbers) and powerball == winningPowerball):
        print()
        print("You have won the powerball Lottery! Congratulations.")
        break
    else:
        print(" You Lost.")
print(f"You have wasted {price}")
print("Thanks for playing")

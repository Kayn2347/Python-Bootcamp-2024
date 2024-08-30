import random

def select_computer_action():
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    return computer_action

def determine_winner(p_computer_action, p_user_action):
    if p_user_action == p_computer_action:
        print(f"Both players selected {p_user_action}. It's a tie!")
    elif p_user_action == "rock":
        if p_computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif p_user_action == "paper":
        if p_computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif p_user_action == "scissors":
        if p_computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")



while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    computer_action = select_computer_action()
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    determine_winner(computer_action, user_action)   
    play_again = input("Play again (Y/N)? ")
    if play_again != "Y":
        break

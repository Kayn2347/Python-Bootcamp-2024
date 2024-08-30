from questions import quiz
from art import logo
from replit import clear

# For checking question answers
def check_answer(question_num, answer, attempts, player):
    clear()
    correct_answer = quiz[question_num] ["answer"]  
    if correct_answer.lower() == answer.lower():
         print(f"Correct Answer! \n{player}'s score is {player_score[player] +1} ")
         return True
    else:
           print(f"Wrong Answer :( \n You have {attemps -1} attemps left! \nTry Again...")
           return False

# For switching users
def switch_users(p_user_index):
    if p_user_index == 0:
        return 1
    return 0


#find Winner
def find_winner(player1, player2):
    if player_score[player1] > player_score[player2]:
       print(f"{player1} Won! The score is {player_score[player1]}")
    elif player_score[player1] < player_score[player2]:
        print(f"{player2} Won! The score is {player_score[player2]}")
    else:
        print("It is DRAW!")


print(logo)
print(f"There are a total of 6 questions, you can skip a question anytime by typing 'skip' ")
input("Press any key to get started...")
players = input("Enter 2 players with space:")
player_list = players.split(" ")
player_score = dict.fromkeys(player_list, 0)
current_player = player_list[0] #staring with first player

for question in quiz:
    print("----------------------")
    print(f"It is {current_player}'s turn.")
    attemps = 2
    while attemps > 0:
        print(quiz[question] ["question"])
        answer = input("Enter answer(To move to the next question, type 'skip'):")
        if answer == "skip":
          break
        check = check_answer(question, answer, attemps, current_player)
        if check:
            player_score[current_player] += 1
            break
        else: 
            attemps -= 1

    current_player_index  = player_list.index(current_player)
    next_player_index = switch_users(current_player_index)
    current_player = player_list[next_player_index]
find_winner(player_list[0], player_list[1])
show_correct_answers = input("Do you want to see the correct answers? (Y/N)")
if show_correct_answers == "Y":
    for question_num, nested_dic in quiz.items():
        for key, value in nested_dic.items():
            print(key + ": ", value)
print("Thanks for playing!")         
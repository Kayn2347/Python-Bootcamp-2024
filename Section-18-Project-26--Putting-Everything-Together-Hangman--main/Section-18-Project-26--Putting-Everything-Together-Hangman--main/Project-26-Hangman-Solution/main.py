# Todo 1
# word_list = ["UDEMY", "APPMILLERS", "PYTHON"]

# import random

# secret_word = random.choice(word_list)
# length_word = len(secret_word)
# blanks = []

# for _ in range(length_word):
#     blanks.append("_")

# print(blanks)

# guess = input("Guess a letter:").upper()

# guessed_letters = []
# if guess in guessed_letters:
#     print("You aldready guessed this letter ")
# else:
#     guessed_letters.append(guess)

# for letter in secret_word:
#     if guess == letter:
#         print("Exist")
#     else:
#         print("Not exist")


# word_list = ["UDEMY", "APPMILLERS", "PYTHON"]

# import random

# secret_word = random.choice(word_list)
# length_word = len(secret_word)
# blanks = []

# for _ in range(length_word):
#     blanks.append("_")

# print(blanks)

# guess = input("Guess a letter:").upper()

# guessed_letters = []
# if guess in guessed_letters:
#     print("You aldready guessed this letter ")
# else:
#     guessed_letters.append(guess)

# for position in range(length_word):
#     letter = secret_word[position]
#     if guess == letter:
#          blanks[position] = letter

# print(blanks)

import random
from logo_stages import hangman_stages, logo
# from hangman_words import word_list
from replit import clear
print(logo)
word_list = ["APPMILLERS", "UDEMY"]
secret_word = random.choice(word_list)
word_length =len(secret_word)
guessed_letters = []
blanks = []
lives = 6
for _ in range(word_length):
    blanks.append("_")
end_game = False
while not end_game:
    guess = input("Guess a letter: ").upper() 
    clear()
    if guess in guessed_letters:
        print("You have already guessed this letter!")
        continue
    else:
        guessed_letters.append(guess)

    for position in range(word_length):
        letter = secret_word[position]
        if guess == letter:
            blanks[position] = letter
    if guess not in secret_word:
        lives -= 1
        if lives == 0:
            end_game = True
            print("You Lose.")

    print(" ".join(blanks))
    # TODO 2
    print(hangman_stages[lives])
    if "_" not in blanks:
        end_game = True
        print("You win")
    # TODO 1
    if end_game:
        ask = input("Do you want to play again?(Y/N) ")
        if ask == "Y":
            secret_word = random.choice(word_list)
            blanks.clear()
            word_length =len(secret_word)
            for _ in range(word_length):
                blanks.append("_")
            end_game = False
            guessed_letters.clear()
            lives = 6
        else:
            print("See you next time.")



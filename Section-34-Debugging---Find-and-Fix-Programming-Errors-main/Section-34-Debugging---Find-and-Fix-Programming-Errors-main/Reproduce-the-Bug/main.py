# Reproduce the bug
import random

deck_cards = ["Heart", "Dimond", "Spade", "Club"]

def custom_function():
    random_card = random.randint(1,4)
    print(deck_cards[random_card])

custom_function()
